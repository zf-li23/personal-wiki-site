---
title: Web 应用与前后端分离
description: Web 应用如何工作（HTTP 请求与响应、方法、状态码、服务器端渲染与单页应用）；何时、为何分离前端与后端，以及分离后的系统如何部署（分离的源、反向代理、CDN）；API 约定（作为契约的 API、OpenAPI、JSON、错误、分页、版本）；基于 Cookie 与会话、持有者令牌与 JWT、OAuth 2.0 的认证与授权；以及每个 Web 开发者都必须处理的安全问题：不可信输入、注入、XSS、同源策略与 CORS，以及 CSRF。
source_hash: 8f520f57586b
---

[4.14.6](/4.14.6) 的架构描述了大型互联网服务如何组织；本章下沉到多数开发者工作的层面：单个 Web 应用，拥有基于浏览器的用户界面，以及一个保存数据的服务器。自 2010 年代以来，这类应用通常采用前后端分离的方式构建：用户界面是自成一体的程序，运行在浏览器（或手机）中，只通过 API 与服务器交谈。本章解释底层的协议（HTTP）、分离何时以及为何值得、分离后的系统如何部署、使 API 成为两个团队之间可靠契约的各种约定、无状态的协议如何被用来记住用户是谁，以及把 API 暴露到互联网上所带来的安全问题。接下来的两章构建这两半：[4.14.8](/4.14.8) 的 React 前端和 [4.14.9](/4.14.9) 的 Django 后端。一个小例子贯穿这三章：一个留言板，其后端提供 API `/api/messages/`，前端列出并发布留言。所展示的全部 HTTP 交互都由该后端产生（Django 6.1 与 Django REST framework 3.18），并去掉了无关紧要的头部。

## 7.1. Web 应用如何工作

### 7.1.1. 浏览器、服务器与 HTTP

Web 应用由客户端（通常是浏览器）和服务器（监听某个网络端口的程序）组成。它们通过 HTTP 通信。

**定义 7.1.1（HTTP）** **超文本传输协议**（HTTP）是 Web 的应用层协议。客户端发送请求（request），它由方法（如 `GET` 或 `POST`）、目标（URL 的路径与查询部分，如 `/api/messages/?page=2`）、头部字段（形如 `Name: value` 的行，携带 `Content-Type`、`Authorization` 或 `Cookie` 之类的元数据）和可选的消息体组成；服务器以响应（response）作答，它由三位数的状态码、头部字段和可选的消息体组成。HTTP 是无状态的：每个请求都独立理解，不参照先前的请求。

HTTP 的语义（方法、状态码、头部）由 RFC 9110 规定，在所有版本中都相同；各版本的差别在于消息如何传输。HTTP/1.1 通过 TCP 连接发送文本消息，每个连接一次只进行一次交互；HTTP/2 以二进制分帧在一个连接上多路复用多次交互；HTTP/3 运行在 QUIC 之上，这是建立在 UDP 上的传输协议，避免了 TCP 的队头阻塞。HTTPS 是 TLS 之上的 HTTP，它对连接加密并认证；每个生产环境的 Web 应用都应当使用它，而且浏览器把许多特性（安全 Cookie、service worker）限制在 HTTPS 下。传输的细节属于计算机网络。

用 `curl -i` 与留言板后端进行的一次交互如下所示。请求创建一条留言；响应以状态 `201 Created` 报告成功，并以 JSON 返回新资源：

```http
POST /api/messages/ HTTP/1.1
Host: 127.0.0.1:8000
Authorization: Token 71f108dd0617a960e928b5820fbbf7c0c9554303
Content-Type: application/json

{"content": "  Posted with a token  "}
```

```http
HTTP/1.1 201 Created
Content-Type: application/json
X-Frame-Options: DENY
X-Content-Type-Options: nosniff

{"id":4,"author":"alice","content":"Posted with a token","created_at":"2026-10-21T12:53:52.386793Z"}
```

响应中有两点已经值得注意。服务器去掉了内容两端的空格；作者是 `alice`，即令牌的所有者，尽管客户端从未发送作者：决定存储什么的是服务器，而不是客户端（7.5.1）。`X-` 开头的头部是 Django 默认添加到每个响应中的安全头部。

### 7.1.2. 方法与状态码

方法表明客户端想对目标资源做什么。

**定义 7.1.2（安全方法与幂等方法）** 若一个 HTTP 方法基本上是只读的，即客户端既不请求、也不期望服务器上发生任何状态变化，则该方法是**安全方法**。若多个相同请求对服务器产生的预期效果与单个请求相同，则该方法是**幂等方法**。

安全性告诉缓存、爬虫和浏览器它们可以自行做什么：浏览器可以预取链接（`GET`），但绝不能不经询问就重复提交表单（`POST`）。幂等性告诉客户端超时之后可以做什么：它可以直接重发 `PUT` 或 `DELETE`，因为无论第一次尝试是否到达了服务器，结果都相同，但不能盲目重发 `POST`，因为那可能创建两份订单。需要安全重试 `POST` 的 API 接受幂等键（idempotency key），即由客户端选定、由服务器记住的唯一请求 ID。

| 方法 | 在 API 中的典型含义 | 安全 | 幂等 | 请求体 |
|---|---|---|---|---|
| `GET` | 读取资源或列出集合 | 是 | 是 | 无 |
| `HEAD` | 类似 `GET`，只要头部 | 是 | 是 | 无 |
| `OPTIONS` | 询问允许哪些方法（CORS 预检，7.5.3） | 是 | 是 | 无 |
| `POST` | 在集合中创建资源，或执行某个操作 | 否 | 否 | 有 |
| `PUT` | 整体替换资源 | 否 | 是 | 有 |
| `PATCH` | 修改资源的某些字段 | 否 | 否（一般而言） | 有 |
| `DELETE` | 删除资源 | 否 | 是 | 很少有 |

状态码表明结果；它的第一位数字给出类别。

| 状态码 | 含义 | 在 API 中的典型用法 |
|---|---|---|
| `200 OK` | 成功 | `GET`，或返回资源的更新 |
| `201 Created` | 已创建资源 | 对集合的 `POST`；`Location` 头部给出其 URL |
| `204 No Content` | 成功，没有消息体 | `DELETE` |
| `301`、`308` | 永久移动 | URL 被改名 |
| `304 Not Modified` | 缓存的副本仍然有效 | 带 `If-None-Match` 的条件 `GET` |
| `400 Bad Request` | 请求格式错误或无效 | 校验错误 |
| `401 Unauthorized` | 未认证（没有或凭据无效） | 令牌缺失或过期 |
| `403 Forbidden` | 已认证，但不被允许 | 删除别人的留言 |
| `404 Not Found` | 没有这个资源 | 未知的 ID；也用来隐藏资源的存在 |
| `405 Method Not Allowed` | 资源不支持该方法 | 对集合执行 `DELETE` |
| `409 Conflict` | 请求与当前状态冲突 | 用户名重复、编辑了过期的版本 |
| `422 Unprocessable Content` | 格式良好但语义无效 | 校验错误（某些框架） |
| `429 Too Many Requests` | 超出速率限制 | `Retry-After` 头部说明何时重试 |
| `500 Internal Server Error` | 服务器中未处理的错误 | 程序缺陷 |
| `502`、`503`、`504` | 网关没有得到有效响应、服务不可用、网关超时 | 反向代理背后的失效、过载、维护 |

`4xx` 状态码表示客户端应当修改请求；`5xx` 状态码表示服务器出了故障，同样的请求稍后可能成功。保持这一区分，客户端、代理和监控（[4.14.13](/4.14.13)）才能作出正确的反应。`401` 的命名是历史的偶然：它的意思是“未认证”，而 `403` 的意思是“未授权”。

### 7.1.3. 在服务器还是在浏览器中渲染

HTML 是在哪里构建的？在经典的服务器端渲染（server-side rendering）模型中，每次点击都发送一个请求，服务器运行代码，把数据填入 HTML 模板（Django 模板、带 Jinja 的 Flask、PHP、Ruby on Rails），返回完整的页面，浏览器显示它并替换之前的页面。浏览器是瘦客户端，全部逻辑都在服务器上。

**定义 7.1.3（单页应用）** **单页应用**（SPA）是这样的 Web 应用：它一次性加载一个 HTML 页面和一个 JavaScript 程序，此后在浏览器中更新页面：程序渲染用户界面，通过 API（通常是基于 HTTP 的 JSON）获取和发送数据，并借助浏览器的 History API 改变 URL 而不加载新页面。

在这两个极端之间，现代框架混合了各种做法：静态站点生成（static site generation）在构建时生成每个页面的 HTML（本维基即如此构建）；带水合（hydration）的服务器端渲染为首个视图发送完整的 HTML，显示快、易于被搜索引擎索引，随后附加使其变成 SPA 的 JavaScript；React 服务器组件（React Server Components）让某些组件只在服务器上运行（[4.14.8](/4.14.8#sec-8.6.3)）。

| | 服务器端渲染 | 单页应用 |
|---|---|---|
| HTML 在哪里构建 | 在服务器上，每个请求一次 | 在浏览器中 |
| 服务器返回什么 | HTML 页面 | 先是一次静态文件，之后是 JSON |
| 首次页面加载 | 快；HTML 完整 | 较慢：要先下载并运行 JavaScript |
| 之后的导航 | 整页重新加载 | 即时，只获取数据 |
| 交互性 | 没有额外的 JavaScript 时有限 | 丰富：UI 就是程序 |
| 搜索引擎 | 直接索引 HTML | 需要预渲染或 SSR |
| 其他客户端（移动应用） | 需要另一套 API | 使用同一套 API |
| 典型技术栈 | Django 或 Rails 模板 | React、Vue 或 Svelte + API 后端 |

## 7.2. 前后端分离

### 7.2.1. 分离何时值得

分离并不总是正确的选择，而其理由最好通过需求如何增长来看清。设想一个网站，向某个院系约两千名学生分发大语言模型 API 的访问权限。用户通过大学的 OAuth 服务登录（7.4.4）；一个静态页面列出可用的模型，另一个页面显示当前用户的令牌与用量。几百行服务器代码加上 HTML 模板，也许借助 AI 助手生成，就能满足这些需求；整个应用比前端框架的默认项目还小，把它分离只会增加工作量。

现在让需求增长：服务向全校开放，用户十万；其中大多数不是程序员，需要可与商业聊天产品相媲美的精致界面；必须有移动网页界面、即时通讯应用内的小程序和桌面客户端；开发者还应能通过公共 API 调用该服务。于是：

- 界面需要复杂的交互和流畅的体验，因而需要现代前端框架；
- 页面加载时间不再允许对每个请求渲染模板：界面必须是从**内容分发网络**（CDN，[4.14.6](/4.14.6#sec-6.8.3)）提供的静态文件；
- 后端需要伸缩，也许要用更快的语言重写，并作为若干相同的副本运行在 Kubernetes 之类的集群上，这要求它是无状态的，全部状态都放在数据库里；
- 若干不同的客户端必须调用同一个后端；
- 独立的前端团队和后端团队必须能够同时工作，而服务器端模板把两种关注点混在同一个文件中，使这一点难以做到。

需求驱动架构：这些**非功能需求**（[4.14.4](/4.14.4)）导向了分离。

**定义 7.2.1（前后端分离）** 在**前后端分离**中，Web 应用被拆分为前端和后端：前端是渲染用户界面并处理交互的客户端程序（单页应用、移动或桌面应用），后端是实现业务逻辑并拥有持久数据的服务器，它只通过 API（通常是基于 HTTP 的 JSON）暴露这些数据。两者独立地开发、构建、测试和部署，API 是它们之间唯一的契约。

| 好处 | 原因 |
|---|---|
| 并行开发 | API 一经商定，前端团队和后端团队就各自独立地工作，每方都针对对方的模拟（mock） |
| 灵活的技术 | 前端专注于交互，后端专注于性能和业务规则；任何一方的技术栈都可以替换而不触及另一方 |
| 多种客户端 | 网页、移动和桌面前端以及第三方开发者使用同一套 API |
| 灵活的部署 | 前端是 CDN 上的静态文件；后端作为负载均衡器（[4.14.6](/4.14.6#sec-6.5.6)）背后的若干副本运行 |

代价同样真实：两套代码库、构建流水线和部署；必须设计、记录并保持兼容的 API；跨源的认证（7.4、7.5.3）；较慢的首次加载以及在搜索引擎可见性上更多的工作；还有重复的逻辑，因为输入检查既出现在前端以方便用户，又出现在后端以保证正确。对于只有一个客户端的小型内部工具，服务器端渲染的应用（带模板的 Django，也许加一点 JavaScript）仍然是更简单、往往也更好的设计。

### 7.2.2. 部署架构

分离后的应用有两类服务器：一类交付前端的静态文件（HTML、JavaScript、CSS、图片），另一类应答 API 请求。它们可以用两种方式暴露。第一种，浏览器直接与每一个交谈，二者位于两个不同的源（例如 `app.example.com` 和 `api.example.com`）：

```mermaid
sequenceDiagram
  actor U as 用户
  participant B as 浏览器
  participant F as 前端服务器（静态文件，CDN）
  participant A as 后端服务器（API）
  U->>B: 打开网站
  B->>F: 1. 请求页面及其脚本
  F-->>B: 2. HTML、JavaScript、CSS
  B->>B: 运行前端程序
  B->>A: 3. API 请求（跨源）
  A-->>B: 4. JSON 数据
  B-->>U: 5. 渲染后的页面
```

由于 API 位于另一个源，后端必须显式允许前端的源（CORS，7.5.3）。在第二种安排中，反向代理把两者放在同一个源之后。

**定义 7.2.2（反向代理）** **反向代理**是这样的服务器：它代表一个或多个后端服务器接收来自客户端的请求，按规则（例如按路径前缀）把每个请求转发给某个后端服务器，并把响应当作自己的一样返回。（相对地，正向代理代表客户端行事。）

```mermaid
sequenceDiagram
  actor U as 用户
  participant B as 浏览器
  participant P as 反向代理（example.com）
  participant F as 静态文件
  participant A as 后端服务器
  U->>B: 打开 https://example.com/
  B->>P: 1. GET /
  P->>F: 转发
  F-->>P: HTML、JavaScript
  P-->>B: 2. 前端文件
  B->>P: 3. GET /api/messages/
  P->>A: 4. 转发 /api/*
  A-->>P: 5. JSON 数据
  P-->>B: 6. 转发响应
  B-->>U: 7. 渲染后的页面
```

代理（Nginx、Caddy、Traefik，或云服务商的负载均衡器）还负责终结 TLS、压缩响应、缓存静态文件、限制请求速率，并把 API 请求分散到若干后端副本上。在开发中，前端工具的开发服务器扮演这一角色：Vite 把 `/api` 转发给 Django 开发服务器（[4.14.8](/4.14.8#sec-8.4.2)）。规模更大时，这些部件就成为第二种场景的架构：

```mermaid
flowchart LR
  subgraph Clients[客户端]
    W[Web 前端]
    M[移动应用]
    D[桌面客户端]
  end
  CDN[CDN：静态资源]
  GW[API 网关 / 负载均衡器]
  subgraph K[Kubernetes 集群]
    P1[后端 pod 1]
    P2[后端 pod 2]
    P3[后端 pod 3]
  end
  DB[(数据库)]
  W --> CDN
  W --> GW
  M --> GW
  D --> GW
  GW --> P1
  GW --> P2
  GW --> P3
  P1 --> DB
  P2 --> DB
  P3 --> DB
```

后端副本之所以可以互换，是因为它们在内存中不保存会话状态：任何必须在请求之后仍然存在的东西，都放在数据库或共享缓存中。这正是 **REST**（[4.14.6](/4.14.6#sec-6.4.1)）的无状态约束在运维上的回报。

## 7.3. API 设计约定

### 7.3.1. 作为契约的 API

在分离之下，API 是两个团队之间的接口，也是他们的误解暴露的地方，所以应当在任何一方实现之前就设计好。API 规格说明对每个操作规定交换数据的格式、前置条件（例如用户必须已登录），以及在什么情形下返回哪些错误。

由于前端是服务用户的一方，一条有用的规则是：由前端的需要驱动 API 设计；后端不应只是把它的表暴露出来。

- 如果前端需要某个用户的简短摘要，后端应当提供 `GET /api/v1/users/42/summary`（或一个 `fields` 参数），而不是让前端下载完整的资料后丢掉大部分。
- 如果前端需要一个用户列表，后端应当提供 `GET /api/v1/users?ids=1,2,3` 或分页列表，而不是让前端循环调用 `GET /api/v1/users/{id}`，那样每个用户都要花一次往返。
- 如果前端必须及时得知新留言，后端应当提供专为此设计的机制，如长轮询（`GET /api/v1/messages/poll`，服务器把它保持打开，直到有消息到达或超时）、服务器发送事件（server-sent events）或 WebSocket，而不是让前端每秒轮询 `GET /api/v1/messages`。

这条规则有其限度：恰好按某一个界面塑造的 API，会在界面改变时失效，对其他客户端的服务也很差。有多个差别很大的客户端的团队，有时给每个客户端各配一个薄的服务器端适配器（前端专用后端，backend for frontend 模式），或者使用 GraphQL，由客户端在每次查询中准确声明它需要哪些字段。

契约怎样书写，不如它被写下来、随代码做版本管理并由机器检查重要。常见的选择有：

- *OpenAPI* 描述（旧称 Swagger；当前版本 3.2），一份 YAML 或 JSON 文档，列出路径、操作、参数、请求和响应的模式以及安全方案，工具据此生成文档、客户端代码、模拟服务器和测试；许多框架可以从代码生成它（Django REST framework 用 drf-spectacular，FastAPI 原生支持）；
- Postman、Apifox 或 Bruno 之类的 API 平台，它们保存示例请求、模拟和测试的集合；
- 共享的类型：前端的 TypeScript 接口与后端的类型注解或序列化器保持同步，也可以从 OpenAPI 描述生成，并配以大量注释。

留言板 API 的 OpenAPI 描述节选：

```yaml
openapi: 3.1.0
info: { title: Message board API, version: 1.0.0 }
paths:
  /api/messages/:
    get:
      summary: List messages, newest first
      parameters:
        - { name: page, in: query, schema: { type: integer, minimum: 1 } }
      responses:
        "200":
          description: One page of messages
          content:
            application/json:
              schema: { $ref: "#/components/schemas/MessagePage" }
    post:
      summary: Post a message as the authenticated user
      security: [{ token: [] }]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [content]
              properties:
                content: { type: string, minLength: 1, maxLength: 280 }
      responses:
        "201": { description: Created }
        "400": { description: Invalid content }
        "401": { description: Not authenticated }
components:
  securitySchemes:
    token: { type: apiKey, in: header, name: Authorization }
```

### 7.3.2. 资源、URL 与 JSON

对多数 Web API，推荐的风格是 **REST**（[4.14.6](/4.14.6#sec-6.4.1)）：URL 命名资源（复数名词，`/api/messages/`、`/api/messages/4/`），HTTP 方法命名操作。针对其他需求也有替代方案：GraphQL 让客户端通过一个端点查询带类型的数据图，而 gRPC（[4.14.6](/4.14.6#sec-6.4.2)）是内部服务之间的常见选择。几乎所有 Web API 的数据格式都是 JSON。


**定义 7.3.1（JSON）** **JSON**（JavaScript Object Notation，RFC 8259）是一种结构化数据的文本格式。JSON 值是对象（花括号中无序的名称-值对集合，名称为字符串）、数组（方括号中有序的列表）、数（number）、字符串（Unicode，用双引号括起）、`true`、`false` 或 `null`。

每种语言都把 JSON 映射到自己的类型：在 Python 中，`json.loads` 把对象变成 `dict`、把数组变成 `list`，`json.dumps` 则相反；在 JavaScript 中是 `JSON.parse` 和 `JSON.stringify`。由于 JSON 没有日期、十进制金额或大整数的类型，API 必须为它们确定约定：

- 时间戳用带时区的 ISO 8601 字符串，`"2026-10-21T12:53:52.386793Z"`，绝不使用不带偏移量的本地时间；
- 金额用最小单位（分）的整数，或用十进制字符串，绝不用二进制浮点数；
- 如果 JavaScript 客户端必须读取 64 位 ID，就用字符串表示，因为 JavaScript 的数只能精确表示不超过 $2^{53}$ 的整数；
- 字段名统一使用一种命名风格（`snake_case` 或 `camelCase`）；
- 显式的 `null` 与缺失字段：决定它们是否表示同一件事，并写入文档。

### 7.3.3. 错误

错误响应应当使用正确的状态码（7.1.2），以及程序可以据以行动、人也能看懂的消息体。对于违反校验规则的请求，Django REST framework 返回：

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{"author":["This field may not be blank."],"content":["This field may not be blank."]}
```

按字段给出的错误让前端能够把每条消息显示在对应的输入框旁边。一种标准的、与框架无关的格式是 RFC 9457 的问题详情（problem details）对象（媒体类型 `application/problem+json`），其成员有 `type`（标识问题种类的 URI）、`title`、`status`、`detail` 和 `instance`，还可以用自己的成员扩展。一种常见的反模式是对每个请求都回答 `200 OK`，而把应用特定的错误码放在消息体里（`{"code": -1, "info": "Bad param"}`）：它向缓存、代理、监控以及每个通用 HTTP 客户端隐藏了失败，而它们都依赖状态码。消息体中的应用级错误码应当作为状态码之外的补充，而不是取代状态码。

### 7.3.4. 分页

可能增长的集合必须分页返回。

| | 偏移量（页码） | 游标（键集） |
|---|---|---|
| 请求 | `?page=3&page_size=20` 或 `?offset=40&limit=20` | `?cursor=eyJpZCI6NDB9`（不透明） |
| 实现 | `LIMIT 20 OFFSET 40` | `WHERE (created_at, id) < (:t, :id) ORDER BY ... LIMIT 20` |
| 跳到第 $n$ 页 | 可以 | 不可以，只能前进和后退 |
| 深页的代价 | 随偏移量增长 | 有索引时为常数 |
| 翻页期间有条目插入 | 条目被跳过或重复 | 稳定 |
| 典型用途 | 管理后台的表格 | 信息流、无限滚动、大型集合 |

留言板使用页码；它的列表响应带有总数和指向相邻页面的链接：

```json
{"count": 4, "next": null, "previous": null,
 "results": [{"id": 4, "author": "alice", "content": "Posted with a token",
              "created_at": "2026-10-21T12:53:52.386793Z"}]}
```

### 7.3.5. 版本管理

已部署的客户端无法同时全部更新（移动应用可能数年不更新），所以 API 只要可能就以兼容的方式变化：增加可选字段和新端点，绝不重命名或删除字段，也不改变其含义。破坏性变更要有新版本，体现在路径（`/api/v2/`）、头部或媒体类型中，并且旧版本在公布的期限内继续受到支持。反过来，客户端应当忽略它们不认识的字段。

## 7.4. 认证与授权

### 7.4.1. 无状态协议之上的身份

早期的 Web 是无状态的：每个请求都是独立的，相同的请求得到相同的响应。应用很快就必须区分用户，但 HTTP 没有用户或登录的概念。因此必须有某种机制在每个请求中携带身份。必须把两个问题分开。

**定义 7.4.1（认证与授权）** **身份认证**是对客户端是谁的验证：通过检查密码、令牌、证书或第二因素，确认请求来自某个特定的用户（或服务）。**授权**（访问控制）是对已认证的身份能否对某个特定资源执行某个特定操作的决定。

留言板体现了这两者。不带凭据发布留言会在认证上失败，Django REST framework 以 `401` 回答，并带有一个 `WWW-Authenticate` 头部，告诉客户端应使用哪种方案：

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json
WWW-Authenticate: Token

{"detail":"Authentication credentials were not provided."}
```

已认证的 Alice 试图删除 Bob 的留言，则通过了认证，却在授权上失败：

```http
HTTP/1.1 403 Forbidden
Content-Type: application/json

{"detail":"You do not have permission to perform this action."}
```

授权必须对每个对象检查，而不只是对每个端点检查：只验证用户已登录、却不验证留言 2 是否属于该用户的 API，会让任何人只需改变 URL 中的数字就能删除任何留言。这种缺陷称为对象级授权失效（broken object-level authorization），是 API 最常见的严重漏洞，在 OWASP 的列表中位居榜首（7.5.5）。

密码本身绝不存储，只存储它的带盐慢哈希，用专为此设计的函数（PBKDF2、scrypt、bcrypt 或 Argon2）计算，而不是用快速的通用**哈希函数**；Django 默认存储 `pbkdf2_sha256$1500000$<salt>$<hash>`，迭代 150 万次，这样即使数据库被盗，密码也不会泄露。

### 7.4.2. Cookie 与会话

**定义 7.4.2（Cookie）** **Cookie** 是服务器通过响应头部 `Set-Cookie` 要求浏览器存储的一个小的名称-值对，只要 Cookie 的属性允许，浏览器之后就会在每个发往同一站点的请求中，通过 `Cookie` 头部自动把它发回。

Cookie 的属性控制它被发送到哪里以及谁能读取它：`Domain` 和 `Path`（哪些请求携带它）、`Max-Age` 或 `Expires`（生存期）、`Secure`（只经由 HTTPS）、`HttpOnly`（JavaScript 无法读取，这使它免遭 XSS 窃取，7.5.2）和 `SameSite`（它是否随其他站点发起的请求一起发送，7.5.4）。

**定义 7.4.3（会话）** 服务器端**会话**是服务器（在数据库、缓存或内存中）保存的一条记录，记录某个用户的交互状态，由一个很长的随机会话 ID（session ID）标识。登录成功之后，服务器通过 Cookie 把会话 ID 交给浏览器；在每个请求中，服务器根据 Cookie 里的 ID 找到会话，从而找到用户。

```mermaid
sequenceDiagram
  participant B as 浏览器
  participant S as 服务器
  participant DB as 会话存储
  B->>S: POST /login（用户名，密码）
  S->>S: 验证密码哈希
  S->>DB: 创建会话 {user: 42}，ID = 9f3c...
  S-->>B: 200 OK，Set-Cookie: sessionid=9f3c...; HttpOnly; Secure; SameSite=Lax
  B->>S: GET /api/messages/（Cookie: sessionid=9f3c...）
  S->>DB: 查找 9f3c...
  DB-->>S: 用户 42
  S-->>B: 200 OK，用户 42 的数据
  B->>S: POST /logout
  S->>DB: 删除会话 9f3c...
```

会话简单，并且默认就是安全的：由浏览器处理 Cookie，`HttpOnly` 的 Cookie 脚本无法触及，而注销（或撤销密码被盗用户的全部会话）就是在服务器上做一次删除。它们的代价是每个请求都要查一次会话存储、后端的所有副本要共用一个会话存储，以及 Cookie 在跨站点和浏览器之外使用时的不便：Cookie 只会自动发送给设置它的站点，跨源请求必须主动选择发送它（`fetch` 中的 `credentials: "include"`，加上服务器的 CORS 许可）。

### 7.4.3. 令牌与 JWT

另一种做法是给客户端一个令牌，由它显式出示。

**定义 7.4.4（持有者令牌）** **持有者令牌**是一种凭据，授予出示它的任何人访问权限，无需再提供其他身份证明。客户端在每个请求中显式发送它，按惯例放在头部 `Authorization: Bearer <token>` 中（RFC 6750）。

令牌可以是不透明的（opaque）：服务器在其数据库中查找的随机字符串（如 Django REST framework 的 `TokenAuthentication`，它使用方案名 `Token` 而不是 `Bearer`）；也可以是自包含的（self-contained）：以签名的形式携带用户的身份，服务器无需任何查找就能验证。标准的自包含令牌是 JWT。

**定义 7.4.5（JSON Web 令牌）** **JSON Web 令牌**（JWT，RFC 7519）是形如 `header.payload.signature` 的紧凑字符串，由三个 Base64url 编码的部分组成：头部（header），一个 JSON 对象，指明签名算法（`"alg": "HS256"`）和类型；载荷（payload），一个 JSON 对象，包含关于主体的声明（claims），例如 `sub`（主体，即用户 ID）、`exp`（过期时间，自 1970 年起的秒数）和 `iat`（签发时间）；以及对前两部分的签名（signature），用只有签发者知道的密钥计算（`HS256` 用共享密钥的 HMAC，`RS256` 和 `ES256` 用私钥）。

下面的 Python 程序只用标准库，签发一个令牌，像任何人都能做的那样读取它，像服务器那样验证它，并拒绝伪造的和过期的令牌：

```python
import base64
import hashlib
import hmac
import json

SECRET = b"server-side-secret"  # known only to the server


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def b64url_decode(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def sign(header: dict, payload: dict) -> str:
    h = b64url(json.dumps(header, separators=(",", ":")).encode())
    p = b64url(json.dumps(payload, separators=(",", ":")).encode())
    mac = hmac.new(SECRET, f"{h}.{p}".encode(), hashlib.sha256).digest()
    return f"{h}.{p}.{b64url(mac)}"


def verify(token: str, now: int) -> dict:
    h, p, s = token.split(".")
    expected = hmac.new(SECRET, f"{h}.{p}".encode(), hashlib.sha256).digest()
    if not hmac.compare_digest(expected, b64url_decode(s)):
        raise ValueError("bad signature")
    header = json.loads(b64url_decode(h))
    if header.get("alg") != "HS256":
        raise ValueError("unexpected algorithm")
    payload = json.loads(b64url_decode(p))
    if payload["exp"] <= now:
        raise ValueError("token expired")
    return payload


token = sign({"alg": "HS256", "typ": "JWT"}, {"sub": "42", "name": "alice", "exp": 1792000000})
print(token)
print(json.loads(b64url_decode(token.split(".")[1])))   # anyone can read the payload
print(verify(token, now=1791990000))

h, p, s = token.split(".")
forged_payload = b64url(json.dumps({"sub": "1", "name": "admin", "exp": 1792000000},
                                   separators=(",", ":")).encode())
for t, now in [(f"{h}.{forged_payload}.{s}", 1791990000), (token, 1792000001)]:
    try:
        verify(t, now)
    except ValueError as e:
        print("rejected:", e)
```

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJhbGljZSIsImV4cCI6MTc5MjAwMDAwMH0.wCglnqCHeql-kPQ7_C4R3QYPGokfNJkgeghh2ChF0_E
{'sub': '42', 'name': 'alice', 'exp': 1792000000}
{'sub': '42', 'name': 'alice', 'exp': 1792000000}
rejected: bad signature
rejected: token expired
```

输出使其本质属性清晰可见。

- JWT 是签名的，不是加密的：Base64url 只是一种编码，任何持有令牌的人都能读取载荷。绝不要把秘密（密码、客户端不应看到的个人数据）放进去。（加密的令牌，即 JWE，也存在，但很少需要。）
- 没有密钥的人无法产生有效的令牌：改变载荷就会使签名失效。比较使用 `hmac.compare_digest`，其运行时间不取决于两个字符串在哪里不同，因此攻击者无法根据计时逐字节猜出签名。
- 服务器必须自己固定所接受的算法，而不是信任头部：那些接受 `"alg": "none"`、或让攻击者把 `RS256` 切换为 `HS256`（把公钥当作 HMAC 密钥）的库，曾造成真实的漏洞。实际中应使用维护良好的库（PyJWT、`djangorestframework-simplejwt`，JavaScript 中的 `jose`），而不是上面这样的代码。
- 验证不需要数据库，这适合无状态的副本和**微服务**（[4.14.6](/4.14.6#sec-6.3.3)）；但出于同样的原因，JWT 在过期之前无法撤销，除非服务器保留一份拒绝名单，而那又把查找带了回来。

通常的折中是使用一对令牌：短期的访问令牌（access token，数分钟）用于授权 API 请求，长期的刷新令牌（refresh token）保管得更谨慎，并对照数据库检查，客户端用它获取新的访问令牌；撤销刷新令牌可使用户在数分钟内登出。浏览器应把令牌存放在哪里，本身也是一个权衡：JavaScript 可读的存储（`localStorage`）暴露于站点上的任何 XSS，而 `HttpOnly` Cookie 脚本无法读取，却把 CSRF 带了回来（7.5.4）。对于与 API 同站点提供的浏览器前端，会话 Cookie 通常是更简单也更安全的选择；令牌适合移动应用、命令行客户端、第三方 API 访问和服务之间的调用。

### 7.4.4. 会话与令牌，以及 OAuth

| | 会话 Cookie | 不透明的持有者令牌 | JWT |
|---|---|---|---|
| 状态在哪里 | 服务器（会话存储） | 服务器（令牌表） | 令牌中 |
| 由谁发送 | 浏览器，自动 | 客户端代码，显式 | 客户端代码，显式 |
| 每个请求是否查找 | 是 | 是 | 否（检查签名） |
| 撤销 | 删除会话 | 删除令牌 | 等待过期，或用拒绝名单 |
| 受 XSS 影响 | 有 `HttpOnly` 时低 | 放在 `localStorage` 中则高 | 放在 `localStorage` 中则高 |
| 受 CSRF 影响 | 是，需要防护 | 否 | 否 |
| 适用于 | 单一站点上的浏览器应用 | API 客户端、脚本 | 分布式服务、联合登录 |

“用”另一个账号（大学账号、GitHub、Google）登录，使用的是 *OAuth 2.0*（RFC 6749，整合于 OAuth 2.1 草案）：这是一种授权框架，用户让某个应用从授权服务器获得访问令牌，而不必把密码交给该应用；还有 *OpenID Connect*，建立在它之上的一层，同时返回一个说明用户是谁的签名 ID 令牌（一个 JWT）。面向 Web 和移动应用的流程是带 PKCE 的授权码流程（authorization code flow with PKCE）：

```mermaid
sequenceDiagram
  actor U as 用户
  participant B as 浏览器
  participant App as 应用后端
  participant AS as 授权服务器
  U->>B: 点击“用大学账号登录”
  B->>AS: 重定向：/authorize?client_id, redirect_uri, scope, state, code_challenge
  AS->>U: 登录页面与授权同意
  U->>AS: 凭据（只在授权服务器上输入）
  AS-->>B: 重定向到 redirect_uri?code=...&state=...
  B->>App: GET /callback?code=...&state=...
  App->>AS: POST /token（code、code_verifier、客户端密钥）
  AS-->>App: 访问令牌、ID 令牌（JWT）
  App->>App: 验证 ID 令牌，创建会话
  App-->>B: Set-Cookie: sessionid=...
```

`state` 参数把回调与应用发出的请求绑定起来（防范登录本身的 CSRF），而 PKCE（一个随机的 `code_verifier`，其哈希作为 `code_challenge` 发送）确保被截获的授权码对其他任何人都没有用处。

## 7.5. 安全

Web 应用中的安全问题并不罕见：大多数事件都由同样的少数几种错误造成，而其中每一种都必须从一开始就设计防范。

### 7.5.1. 绝不信任客户端

前端运行在用户的机器上，完全在用户的控制之下：它的源码可以被修改，浏览器的开发者工具可以改变任何请求，脚本可以不经任何前端直接调用 API。无论前端的检查多么严格，后端都必须把每个请求当作可能是精心构造的。否则用户可以：

- 订购 $-10$ 件商品，或在请求体中把商品价格改为 $-100$；
- 给商品打 $-2147483648$ 星的评分，即最小的 32 位整数，服务器可能把它变成荒谬的或溢出的平均值（**整数溢出**）；
- 设置表单中没有显示的字段，如 `"author": "bob"` 或 `"is_admin": true`（批量赋值，mass assignment），这就是留言板从已认证用户取得作者、而忽略消息体中该字段的原因；
- 通过改变 URL 中的 ID 访问其他用户的对象（7.4.1）。

前端的校验是为了用户方便（即时反馈，不浪费往返）；后端的校验是为了正确与安全。后端对每个请求检查类型、范围、长度、格式、归属和业务规则，用允许名单限定接受的字段，并把其余一切都当作错误。CORS 和 CSRF 防护（见下）并不改变这一点：它们保护的是用户的浏览器，而不是 API，并且没有什么能阻止任何人用 Python 脚本调用 API。

### 7.5.2. 注入与跨站脚本

不可信的输入一旦作为代码而非数据到达解释器，就变得危险。评论 `Wow <script>alert("XSS")</script>` 若未经转义就插入页面，就会在每个访问者的浏览器中作为脚本运行；一个内容为 `<?php system($_GET["cmd"]); ?>` 的文件 `shell.php`，若被上传到 Web 服务器会执行的目录中，就会让攻击者在服务器上得到一个 shell；一个请求 `/user?id=1%3B%20DROP%20DATABASE%3B`（解码后的参数是 `1; DROP DATABASE;`），若被拼进 **SQL** 字符串，就可能毁掉数据库。最后一种是 **SQL 注入**，它及其防御手段**参数化查询**在 [4.13.4](/4.13.4#sec-4.9.2) 中讨论。对每种解释器，一般规则都相同：让代码与数据分开，办法是通过无法解释数据的接口传递数据（查询参数、给 `subprocess` 的参数列表而不是 **Shell** 命令字符串、会转义的模板），并且绝不通过字符串拼接来构造代码。

**定义 7.5.1（跨站脚本）** **跨站脚本**（XSS）是一种注入攻击：攻击者使某个网页包含脚本，受害者的浏览器在该页面所属站点的上下文中执行它，脚本可以访问其数据、未标记 `HttpOnly` 的 Cookie、存储中的令牌，并能以用户的身份发送请求。在存储型 XSS 中，脚本被保存在服务器上（在某条评论里），并提供给每个访问者；在反射型 XSS 中，它藏在请求参数里，由服务器回显到响应中；在基于 DOM 的 XSS 中，前端代码把不可信的数据插入页面本身。

防御是分层的。按上下文转义输出：现代模板引擎（Django 模板）和前端框架（React，[4.14.8](/4.14.8#sec-8.2.2)）默认转义文本，所以危险在于它们显式的逃生口（`|safe`、`mark_safe`、`dangerouslySetInnerHTML`、`innerHTML`）；必须包含 HTML 的富文本要经过 DOMPurify 之类的净化器。添加内容安全策略（Content Security Policy）头部，告诉浏览器允许哪些脚本来源（Django 6 内置了对 CSP 的支持），使被注入的内联脚本无法运行。保持会话 Cookie 为 `HttpOnly`。对于上传，检查类型和大小，把文件存放在可执行的 Web 根目录之外并使用生成的文件名，并以固定的 `Content-Type` 提供它们（以及 `X-Content-Type-Options: nosniff`，Django 默认设置它）。

### 7.5.3. 同源策略与 CORS

**定义 7.5.2（同源策略）** Web 资源的**源**（origin）是其 URL 的协议、主机和端口三元组：`https://app.example.com` 和 `https://api.example.com:443` 是不同的源，`http://localhost:5173` 和 `http://localhost:8000` 也是。浏览器的**同源策略**限制从一个源加载的文档或脚本如何与另一个源的资源交互：特别是，脚本可以向另一个源发送请求，但除非该源允许，否则不能读取响应。

没有这一策略，你访问的任何网页都可以利用已登录的浏览器，读取你在另一个标签页所在站点中的邮件。然而前端与 API 位于不同源的分离式应用，需要一个受控的例外。

**定义 7.5.3（跨源资源共享）** **跨源资源共享**（CORS）是服务器告诉浏览器哪些其他源可以读取其响应的协议。服务器用 `Access-Control-Allow-Origin: https://app.example.com` 之类的头部作答。对于普通 HTML 表单无法发送的请求（`GET`、`HEAD` 和 `POST` 以外的方法，`Authorization` 之类的自定义头部，或 JSON 内容类型），浏览器首先发送方法为 `OPTIONS` 的预检（preflight）请求，仅当服务器的回答允许该方法、头部和源时才发送真正的请求。

从位于 `http://localhost:5173` 的前端发往留言板后端的预检请求，由于后端没有配置 CORS，Django REST framework 会返回正常的 `200`，但没有任何 `Access-Control-Allow-Origin` 头部；浏览器因此拒绝发送 `POST`，并在控制台中报告 CORS 错误：

```http
OPTIONS /api/messages/ HTTP/1.1
Origin: http://localhost:5173
Access-Control-Request-Method: POST
Access-Control-Request-Headers: authorization, content-type
```

```http
HTTP/1.1 200 OK
Content-Type: application/json
Allow: GET, POST, HEAD, OPTIONS

{"name":"Message List","description":"","renders":["application/json","text/html"],"parses":["application/json","application/x-www-form-urlencoded","multipart/form-data"]}
```

有两种正确的补救办法。在服务器上为恰好是前端的源配置 CORS（在 Django 中使用 `django-cors-headers` 包：`CORS_ALLOWED_ORIGINS = ["https://app.example.com"]`）；绝不要把任何 `Origin` 原样回显，也绝不要把通配符与凭据结合使用。或者通过反向代理从同一个源提供前端和 API，从而完全避免跨源请求（7.2.2）。有三个常见的误解。CORS 是对同源策略的放宽，而不是对服务器的保护：缺少 CORS 头部并不能阻止“简单”请求被发送和执行，只能阻止它们的响应被读取。它只由浏览器执行，所以对脚本和其他客户端毫无作用。并且，从同一个源提供一切并不使跨站攻击成为不可能：CSRF 仍然必须处理。

### 7.5.4. 跨站请求伪造

**定义 7.5.4（跨站请求伪造）** **跨站请求伪造**（CSRF）是这样的攻击：恶意站点使受害者的浏览器向受害者已登录的另一个站点发送一个改变状态的请求；由于浏览器自动附上该站点的 Cookie，请求便以受害者的权限被执行，尽管受害者从未有此意图。

只要银行靠 Cookie 认证而没有其他措施，`evil.example` 上的一个页面，包含一个向 `https://bank.example/transfer` 提交的隐藏表单，并用一行 JavaScript 提交它，就足够了。攻击者读不到响应（同源策略），但也不需要读。防御措施有：

- `SameSite` Cookie：设置 `SameSite=Lax` 时（基于 Chromium 的浏览器会对没有设置 `SameSite` 属性的 Cookie 应用它；请显式设置），Cookie 不会随跨站 `POST` 请求发送，设置 `Strict` 时连跨站链接也不发送；
- 防 CSRF 令牌：服务器把一个秘密值放入每个表单，或放入页面的 JavaScript 会复制到头部的 Cookie（Django 的 `csrftoken` Cookie 和 `X-CSRFToken` 头部），并拒绝没有它的改变状态的请求，其他站点无法获得它；
- 对照允许名单检查改变状态的请求的 `Origin`（或 `Referer`）头部，Django 也这样做；
- 保持 `GET` 安全（7.1.2），因为链接和图片会从任何地方触发 `GET` 请求。

Django 的 `CsrfViewMiddleware` 默认启用，它以 `403 Forbidden` 和日志行 `Forbidden (CSRF cookie not set.)` 拒绝了留言板项目中对普通 Django 视图的一次 JSON `POST`，这是防护在起作用，而不是需要用 `@csrf_exempt` 修复的缺陷。只通过显式 `Authorization` 头部认证的 API 不受 CSRF 影响，因为浏览器绝不会自己添加该头部；这就是 Django REST framework 只对会话认证的请求强制执行 CSRF 的原因。

### 7.5.5. 检查清单

OWASP Top 10（2025 年版）根据真实事件的数据，对 Web 应用最关键的风险排序：访问控制失效、安全配置错误、软件供应链失效、加密失效、注入、不安全的设计、认证失效、软件或数据完整性失效、安全日志与告警失效，以及对异常情况的错误处理。OWASP 的速查表对每一项都给出具体指导。适用于本课程各应用的最小检查清单：

| 方面 | 做法 |
|---|---|
| 传输 | 处处使用 HTTPS；HSTS；`Secure` Cookie |
| 输入 | 在服务器上对照允许名单校验每个字段；限制大小 |
| 访问控制 | 在每个视图中检查认证和对象级授权；默认拒绝 |
| 注入 | 参数化查询或 ORM；不用 shell 字符串；不用 `eval` |
| 输出 | 依靠自动转义；净化 HTML；内容安全策略 |
| 会话与令牌 | `HttpOnly`、`SameSite` Cookie；短期令牌；绝不把秘密放进 JWT 载荷 |
| 跨站 | 只对已知的源启用 CORS；对基于 Cookie 的认证启用 CSRF 防护 |
| 秘密 | 密钥和密码放在环境变量或密钥存储中，绝不放进 Git |
| 配置 | 生产环境关闭 `DEBUG`；没有默认凭据；错误页面不含堆栈跟踪 |
| 依赖 | 锁定版本，定期更新，扫描已知漏洞 |
| 日志 | 记录认证失败和访问拒绝，绝不记录密码或令牌 |
| 滥用 | 对登录和开销大的端点做速率限制 |

## 7.6. 智能体编写代码时的分离

只要先有契约，分离就非常适合与**编程智能体**协作。OpenAPI 描述或一组共享类型是精确的、机器可检查的规格说明（[4.14.4](/4.14.4#sec-4.6)），让一个智能体实现后端、另一个智能体实现前端，二者可以并行工作而互不触及对方的文件，每方都针对对方的模拟；随后，用模式校验真实响应的契约测试可以发现两者之间的偏离。安全值得评审者特别留意，因为生成的代码往往恰好犯 7.5 节的那些错误：检查用户已登录却不检查对象是否属于他，把请求的所有字段复制进模型，为了让错误消息消失而禁用 CSRF 或允许所有 CORS 源，并在调试时记录令牌。负面测试（匿名 `POST` 必须得到 `401`，他人的 `DELETE` 必须得到 `403`，超长字段必须得到 `400`）由人在实现之前编写或评审，使这些要求变成智能体无法争辩的检查（[4.14.9](/4.14.9#sec-9.7.2)）。

## 小结

- HTTP 是无状态的请求-响应协议：方法、目标、头部和消息体；状态码、头部和消息体。`GET`、`HEAD`、`OPTIONS` 是安全的；`PUT` 和 `DELETE` 是幂等的，`POST` 不是。`4xx` 状态码归咎于请求，`5xx` 归咎于服务器；`401` 表示未认证，`403` 表示禁止。
- 服务器端渲染对每个请求构建 HTML；单页应用只加载一次，然后获取 JSON。前后端分离把客户端程序与 API 服务器分开，在有多种客户端、丰富交互、独立团队和需要伸缩时值得，代价是一份 API 契约和两套部署。
- 分离后的系统要么部署在两个源上（配合 CORS），要么部署在同一个源的反向代理之后；静态文件放到 CDN，无状态的后端副本放在负载均衡器之后。
- 先设计 API，从客户端的需要出发；把它写成 OpenAPI 或共享类型。使用 REST 风格的资源，JSON 对日期、金额和 ID 有显式约定，有意义的状态码配合结构化的错误消息体（RFC 9457），以及分页和兼容的演化。
- 认证确立身份，授权决定访问，且针对每个对象。会话把状态保存在服务器上并使用 Cookie；持有者令牌被显式发送；JWT 是签名的（可读，不保密），无需查找即可验证，但难以撤销。OAuth 2.0 与 OpenID Connect 委托登录。
- 绝不信任客户端。通过让代码与数据分开来防止注入，通过转义和 CSP 防止 XSS，通过同源策略加严格的 CORS 规则防止跨源读取，通过 `SameSite` Cookie、CSRF 令牌和源检查防止 CSRF。

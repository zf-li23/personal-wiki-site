---
title: Web Applications and Front-End/Back-End Separation
description: "How a web application works (HTTP requests and responses, methods, status codes, server-side rendering and single-page applications); when and why to separate the front end from the back end, and how separated systems are deployed (separate origins, reverse proxies, CDNs); API conventions (the API as a contract, OpenAPI, JSON, errors, pagination, versioning); authentication and authorization with cookies and sessions, bearer tokens and JWT, OAuth 2.0; and the security problems every web developer must handle: untrusted input, injection, XSS, the same-origin policy and CORS, and CSRF."
---

The architectures of [4.14.6](/4.14.6) describe how large Internet services are organized; this chapter descends to the level at which most developers work: a single web application with a browser-based user interface and a server that holds the data. Since the 2010s such applications are usually built with *front-end/back-end separation*: the user interface is a program of its own that runs in the browser (or on a phone) and talks to the server only through an API. The chapter explains the protocol underneath (HTTP), why and when separation pays off and how separated systems are deployed, the conventions that make an API a reliable contract between two teams, how a stateless protocol is made to remember who the user is, and the security problems that come with exposing an API to the Internet. The next two chapters build the two halves: a React front end in [4.14.8](/4.14.8) and a Django back end in [4.14.9](/4.14.9). One small example runs through all three chapters: a message board whose back end offers the API `/api/messages/` and whose front end lists and posts messages. All HTTP exchanges shown were produced by that back end (Django 6.1 with Django REST framework 3.18), with uninteresting headers removed.

## 7.1. How a Web Application Works

### 7.1.1. Browser, Server and HTTP

A web application consists of a *client*, usually a browser, and a *server*, a program that listens on a network port. They communicate by HTTP.

**Definition 7.1.1 (HTTP)** The **Hypertext Transfer Protocol** (HTTP) is the application-level protocol of the Web. A client sends a *request*, which consists of a method (such as `GET` or `POST`), a target (the path and query of a URL, such as `/api/messages/?page=2`), header fields (`Name: value` lines carrying metadata such as `Content-Type`, `Authorization` or `Cookie`) and an optional body; the server answers with a *response*, which consists of a three-digit status code, header fields and an optional body. HTTP is *stateless*: each request is understood on its own, without reference to earlier requests.

The semantics of HTTP (methods, status codes, headers) are specified in RFC 9110 and are the same in all versions; the versions differ in how messages travel. HTTP/1.1 sends text messages over a TCP connection, one exchange at a time per connection; HTTP/2 multiplexes many exchanges over one connection in a binary framing; HTTP/3 runs over QUIC, a transport protocol on UDP that avoids TCP's head-of-line blocking. HTTPS is HTTP over TLS, which encrypts and authenticates the connection; every production web application should use it, and browsers restrict many features (secure cookies, service workers) to HTTPS. The details of the transport belong to computer networks.

An exchange with the message board's back end, made with `curl -i`, looks as follows. The request creates a message; the response reports success with status `201 Created` and returns the new resource as JSON:

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

Two things in the response are worth noticing already. The server trimmed the spaces from the content, and the author is `alice`, the owner of the token, although the client never sent an author: the server decides what is stored, not the client (§7.5.1). The `X-` headers are security headers that Django adds to every response by default.

### 7.1.2. Methods and Status Codes

The method states what the client wants to do with the target resource.

**Definition 7.1.2 (Safe and Idempotent Methods)** An HTTP method is **safe** if it is essentially read-only: the client does not request, and does not expect, any change of state on the server. A method is **idempotent** if the intended effect on the server of several identical requests is the same as that of a single one.

Safety tells caches, crawlers and browsers what they may do on their own: a browser may prefetch a link (`GET`) but must never repeat a form submission (`POST`) without asking. Idempotence tells a client what it may do after a timeout: it may simply resend a `PUT` or a `DELETE`, because the result is the same whether the first attempt reached the server or not, but it must not resend a `POST` blindly, since that might create two orders. APIs that need safe retries of `POST` accept an *idempotency key*, a unique client-chosen request ID that the server remembers.

| Method | Typical meaning in an API | Safe | Idempotent | Request body |
|---|---|---|---|---|
| `GET` | read a resource or list a collection | yes | yes | no |
| `HEAD` | like `GET`, headers only | yes | yes | no |
| `OPTIONS` | ask which methods are allowed (CORS preflight, §7.5.3) | yes | yes | no |
| `POST` | create a resource in a collection, or run an operation | no | no | yes |
| `PUT` | replace a resource entirely | no | yes | yes |
| `PATCH` | change some fields of a resource | no | no (in general) | yes |
| `DELETE` | delete a resource | no | yes | rarely |

The status code states the outcome; its first digit gives the class.

| Code | Meaning | Typical use in an API |
|---|---|---|
| `200 OK` | success | a `GET`, or an update that returns the resource |
| `201 Created` | a resource was created | a `POST` to a collection; `Location` header gives its URL |
| `204 No Content` | success, no body | a `DELETE` |
| `301`, `308` | moved permanently | a renamed URL |
| `304 Not Modified` | the cached copy is still valid | conditional `GET` with `If-None-Match` |
| `400 Bad Request` | the request is malformed or invalid | validation errors |
| `401 Unauthorized` | not authenticated (no or invalid credentials) | missing or expired token |
| `403 Forbidden` | authenticated, but not allowed | deleting someone else's message |
| `404 Not Found` | no such resource | unknown ID; also used to hide that a resource exists |
| `405 Method Not Allowed` | the resource does not support the method | `DELETE` on a collection |
| `409 Conflict` | the request conflicts with the current state | duplicate username, edit of a stale version |
| `422 Unprocessable Content` | well-formed but semantically invalid | validation errors (some frameworks) |
| `429 Too Many Requests` | rate limit exceeded | `Retry-After` header says when to retry |
| `500 Internal Server Error` | an unhandled error in the server | a bug |
| `502`, `503`, `504` | the gateway got no valid response, the service is unavailable, the gateway timed out | failures behind a reverse proxy, overload, maintenance |

The `4xx` codes say that the client should change the request; the `5xx` codes say that the server failed and the same request may succeed later. Keeping this distinction is what lets clients, proxies and monitoring ([4.14.13](/4.14.13)) react correctly. The naming of `401` is a historical accident: it means "unauthenticated", and `403` means "unauthorized".

### 7.1.3. Rendering on the Server or in the Browser

Where is the HTML built? In the classical *server-side rendering* model, every click sends a request, and the server runs code that fills an HTML template with data (Django templates, Flask with Jinja, PHP, Ruby on Rails) and returns a complete page, which the browser displays, replacing the previous one. The browser is a thin client, and all logic lives on the server.

**Definition 7.1.3 (Single-Page Application)** A **single-page application** (SPA) is a web application that loads one HTML page together with a JavaScript program once, and thereafter updates the page in the browser: the program renders the user interface, fetches and sends data through an API (usually JSON over HTTP), and changes the URL with the browser's History API without loading a new page.

Between the two extremes, modern frameworks mix the approaches: *static site generation* builds the HTML of every page at build time (this wiki is built that way); server-side rendering with *hydration* sends complete HTML for the first view, which is fast to display and easy for search engines to index, and then attaches the JavaScript that turns it into an SPA; *React Server Components* run some components only on the server ([4.14.8](/4.14.8#sec-8.6.3)).

| | Server-side rendering | Single-page application |
|---|---|---|
| where HTML is built | on the server, per request | in the browser |
| what the server returns | HTML pages | static files once, then JSON |
| first page load | fast; complete HTML | slower: download and run JavaScript first |
| later navigation | full page reload | instant, only data is fetched |
| interactivity | limited without extra JavaScript | rich: the UI is a program |
| search engines | index the HTML directly | need prerendering or SSR |
| other clients (mobile apps) | need a separate API | use the same API |
| typical stack | Django or Rails templates | React, Vue or Svelte + an API back end |

## 7.2. Front-End/Back-End Separation

### 7.2.1. When Separation Pays Off

Separation is not always the right choice, and the reasons for it are best seen through how requirements grow. Consider a website that distributes access to large language model APIs to the students of one department, some two thousand people. Users log in through the university's OAuth service (§7.4.4); one static page lists the available models, and another shows the current user's token and usage. A few hundred lines of server code with HTML templates, perhaps generated with an AI assistant, meet these requirements; the whole application is smaller than the default project of a front-end framework, and separating it would only add work.

Now let the requirements grow: the service is opened to the whole university, a hundred thousand users; most of them are not programmers and need a polished interface comparable to commercial chat products; there must be a mobile web interface, a mini program inside a messaging app and desktop clients; and developers should be able to call the service through a public API. Then:

- the interface needs complex interaction and a smooth experience, hence a modern front-end framework;
- page load time no longer allows rendering templates per request: the interface must be static files served from a content delivery network (CDN, [4.14.6](/4.14.6#sec-6.8.3));
- the back end needs to scale, perhaps to be rewritten in a faster language, and to run as several identical replicas on a cluster such as Kubernetes, which requires it to be stateless, with all state in the database;
- several different clients must call the same back end;
- separate front-end and back-end teams must be able to work at the same time, which server-side templates, mixing both concerns in one file, make difficult.

Requirements drive the architecture: these non-functional requirements ([4.14.4](/4.14.4)) lead to separation.

**Definition 7.2.1 (Front-End/Back-End Separation)** In **front-end/back-end separation**, a web application is split into a *front end*, the client-side program that renders the user interface and handles interaction (a single-page application, a mobile or desktop app), and a *back end*, a server that implements the business logic and owns the persistent data, which it exposes only through an API (usually HTTP with JSON). The two are developed, built, tested and deployed independently, and the API is the only contract between them.

| Benefit | Why |
|---|---|
| parallel development | once the API is agreed, front-end and back-end teams work independently, each against a mock of the other |
| flexible technology | the front end concentrates on interaction, the back end on performance and business rules; either stack can be replaced without touching the other |
| several clients | web, mobile and desktop front ends and third-party developers use one API |
| flexible deployment | the front end is static files on a CDN; the back end runs as replicas behind a load balancer ([4.14.6](/4.14.6#sec-6.5.6)) |

The costs are just as real: two code bases, build pipelines and deployments; an API that must be designed, documented and kept compatible; authentication across origins (§7.4, §7.5.3); a slower first load and more work for search-engine visibility; and duplicated logic, since input checks exist in the front end for the user's convenience and again in the back end for correctness. For a small internal tool with one client, a server-rendered application (Django with templates, perhaps with a little JavaScript) is still the simpler and often better design.

### 7.2.2. Deployment Architectures

A separated application has two kinds of servers: one that delivers the front end's static files (HTML, JavaScript, CSS, images) and one that answers API requests. They can be exposed in two ways. In the first, the browser talks to each directly, at two different origins (for example `app.example.com` and `api.example.com`):

```mermaid
sequenceDiagram
  actor U as User
  participant B as Browser
  participant F as Front-end server (static files, CDN)
  participant A as Back-end server (API)
  U->>B: Open the site
  B->>F: 1. Request the page and its scripts
  F-->>B: 2. HTML, JavaScript, CSS
  B->>B: Run the front-end program
  B->>A: 3. API request (cross-origin)
  A-->>B: 4. JSON data
  B-->>U: 5. Rendered page
```

Because the API is at another origin, the back end must allow the front end's origin explicitly (CORS, §7.5.3). In the second arrangement, a reverse proxy puts both behind a single origin.

**Definition 7.2.2 (Reverse Proxy)** A **reverse proxy** is a server that receives requests from clients on behalf of one or more back-end servers, forwards each request to a back-end server according to rules (for example by path prefix), and returns the responses as if they were its own. (A forward proxy, by contrast, acts on behalf of clients.)

```mermaid
sequenceDiagram
  actor U as User
  participant B as Browser
  participant P as Reverse proxy (example.com)
  participant F as Static files
  participant A as Back-end server
  U->>B: Open https://example.com/
  B->>P: 1. GET /
  P->>F: forward
  F-->>P: HTML, JavaScript
  P-->>B: 2. Front-end files
  B->>P: 3. GET /api/messages/
  P->>A: 4. Forward /api/*
  A-->>P: 5. JSON data
  P-->>B: 6. Forward the response
  B-->>U: 7. Rendered page
```

The proxy (Nginx, Caddy, Traefik, or the load balancer of a cloud provider) also terminates TLS, compresses responses, caches static files, limits request rates and spreads API requests over several back-end replicas. In development, the dev server of the front-end tool plays this role: Vite forwards `/api` to the Django development server ([4.14.8](/4.14.8#sec-8.4.2)). At a larger scale the pieces become the architecture of the slide's second scenario:

```mermaid
flowchart LR
  subgraph Clients
    W[Web front end]
    M[Mobile app]
    D[Desktop client]
  end
  CDN[CDN: static assets]
  GW[API gateway / load balancer]
  subgraph K[Kubernetes cluster]
    P1[Back-end pod 1]
    P2[Back-end pod 2]
    P3[Back-end pod 3]
  end
  DB[(Database)]
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

The back-end replicas are interchangeable because they keep no session state in memory: anything that must survive a request lives in the database or in a shared cache. This is the statelessness constraint of REST ([4.14.6](/4.14.6#sec-6.4.1)) paying off operationally.

## 7.3. API Design Conventions

### 7.3.1. The API as a Contract

Under separation, the API is the interface between two teams and the place where their misunderstandings surface, so it should be designed before either side is implemented. An API specification states, for each operation, the format of the data exchanged, the preconditions (for example, that the user must be logged in) and which errors are returned in which situations.

Since the front end is the side that serves the users, a useful rule is that the front end's needs drive the API design; the back end should not merely expose its tables.

- If the front end needs a short summary of a user, the back end should offer `GET /api/v1/users/42/summary` (or a `fields` parameter), rather than letting the front end download the full profile and discard most of it.
- If the front end needs a list of users, the back end should offer `GET /api/v1/users?ids=1,2,3` or a paginated list, rather than letting the front end call `GET /api/v1/users/{id}` in a loop, which costs one round trip per user.
- If the front end must learn about new messages promptly, the back end should offer a mechanism made for it, such as long polling (`GET /api/v1/messages/poll`, which the server holds open until a message arrives or a timeout passes), server-sent events or a WebSocket, rather than letting the front end poll `GET /api/v1/messages` every second.

The rule has a limit: an API shaped exactly after one screen breaks when the screen changes and serves other clients poorly. Teams with several very different clients sometimes give each its own thin server-side adapter (the *backend for frontend* pattern), or use GraphQL, in which the client states in each query exactly which fields it needs.

How the contract is written matters less than that it is written, versioned with the code and checked by machines. The common choices are:

- an *OpenAPI* description (formerly Swagger; current version 3.2), a YAML or JSON document listing paths, operations, parameters, request and response schemas and security schemes, from which tools generate documentation, client code, mock servers and tests; many frameworks generate it from the code (drf-spectacular for Django REST framework, FastAPI natively);
- API platforms such as Postman, Apifox or Bruno, which hold collections of example requests, mocks and tests;
- shared types: a TypeScript interface on the front end and type annotations or serializers on the back end, kept in sync, possibly generated from the OpenAPI description, together with many comments.

An excerpt of an OpenAPI description of the message board's API:

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

### 7.3.2. Resources, URLs and JSON

For most web APIs the recommended style is REST ([4.14.6](/4.14.6#sec-6.4.1)): URLs name resources (plural nouns, `/api/messages/`, `/api/messages/4/`), and the HTTP methods name the operations. Alternatives exist for other needs: GraphQL lets clients query a typed graph of data with one endpoint, and gRPC ([4.14.6](/4.14.6#sec-6.4.2)) is the usual choice between internal services. The data format of almost all web APIs is JSON.

**Definition 7.3.1 (JSON)** **JSON** (JavaScript Object Notation, RFC 8259) is a text format for structured data. A JSON value is an object (an unordered set of name–value pairs in braces, with string names), an array (an ordered list in brackets), a *number*, a string (Unicode, in double quotes), `true`, `false` or `null`.

Every language maps JSON to its own types: in Python `json.loads` turns an object into a `dict` and an array into a `list`, and `json.dumps` does the reverse; in JavaScript `JSON.parse` and `JSON.stringify`. Since JSON has no types for dates, decimal amounts or large integers, an API must fix conventions for them:

- timestamps as ISO 8601 strings with a time zone, `"2026-10-21T12:53:52.386793Z"`, never local times without an offset;
- money as an integer number of the smallest unit (cents) or as a decimal string, never as a binary floating-point number;
- 64-bit IDs as strings if JavaScript clients must read them, because a JavaScript number represents integers exactly only up to $2^{53}$;
- one naming style for field names (`snake_case` or `camelCase`), consistently;
- explicit `null` versus an absent field: decide and document whether they mean the same thing.

### 7.3.3. Errors

An error response should use the right status code (§7.1.2) and a body that a program can act on and a person can understand. Django REST framework returns, for a request that violates the validation rules:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{"author":["This field may not be blank."],"content":["This field may not be blank."]}
```

Errors per field let the front end show each message next to the right input. A standard, framework-independent format is the *problem details* object of RFC 9457 (media type `application/problem+json`), with members `type` (a URI identifying the kind of problem), `title`, `status`, `detail` and `instance`, extensible with members of one's own. A common anti-pattern is to answer every request with `200 OK` and put an application-specific error code into the body (`{"code": -1, "info": "Bad param"}`): it hides failures from caches, proxies, monitoring and every generic HTTP client, which all rely on the status code. An application-level code in the body is useful in addition to the status code, not instead of it.

### 7.3.4. Pagination

A collection that can grow must be returned in pages.

| | Offset (page number) | Cursor (keyset) |
|---|---|---|
| request | `?page=3&page_size=20` or `?offset=40&limit=20` | `?cursor=eyJpZCI6NDB9` (opaque) |
| implementation | `LIMIT 20 OFFSET 40` | `WHERE (created_at, id) < (:t, :id) ORDER BY ... LIMIT 20` |
| jump to page $n$ | yes | no, only next and previous |
| cost of deep pages | grows with the offset | constant with an index |
| when items are inserted while paging | items are skipped or repeated | stable |
| typical use | admin tables | feeds, infinite scrolling, large collections |

The message board uses page numbers; its list response carries the total count and links to the neighbouring pages:

```json
{"count": 4, "next": null, "previous": null,
 "results": [{"id": 4, "author": "alice", "content": "Posted with a token",
              "created_at": "2026-10-21T12:53:52.386793Z"}]}
```

### 7.3.5. Versioning

Clients in the field cannot all be updated at once (a mobile app may stay unupdated for years), so an API changes compatibly whenever possible: add optional fields and new endpoints, never rename or remove fields or change their meaning. A breaking change gets a new version, in the path (`/api/v2/`), a header or a media type, and the old version is supported for an announced period. Clients, in turn, should ignore fields they do not know.

## 7.4. Authentication and Authorization

### 7.4.1. Identity over a Stateless Protocol

The early Web was stateless: every request was independent, and the same request gave the same response. Applications soon had to distinguish users, but HTTP has no notion of a user or a login. Some mechanism must therefore carry identity in every request. Two questions must be kept apart.

**Definition 7.4.1 (Authentication and Authorization)** **Authentication** is the verification of who the client is: that the request comes from a particular user (or service), by checking a password, a token, a certificate or a second factor. **Authorization** (access control) is the decision whether an authenticated identity may perform a particular operation on a particular resource.

The message board shows both. Posting without credentials fails authentication, and Django REST framework answers `401` with a `WWW-Authenticate` header that tells the client which scheme to use:

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json
WWW-Authenticate: Token

{"detail":"Authentication credentials were not provided."}
```

Alice, authenticated, trying to delete Bob's message passes authentication but fails authorization:

```http
HTTP/1.1 403 Forbidden
Content-Type: application/json

{"detail":"You do not have permission to perform this action."}
```

Authorization must be checked for every object, not only for every endpoint: an API that verifies that the user is logged in but not that message 2 belongs to them lets anyone delete any message by changing the number in the URL. This flaw, *broken object-level authorization*, is the most common serious vulnerability of APIs and heads the OWASP lists (§7.5.5).

Passwords themselves are never stored, only a slow salted hash of them, computed with a function designed for the purpose (PBKDF2, scrypt, bcrypt or Argon2) rather than a fast general-purpose **hash function**; Django stores `pbkdf2_sha256$1500000$<salt>$<hash>` with 1.5 million iterations by default, so that a stolen database does not reveal the passwords.

### 7.4.2. Cookies and Sessions

**Definition 7.4.2 (Cookie)** A **cookie** is a small name–value pair that a server asks the browser to store, with the response header `Set-Cookie`, and that the browser then sends back automatically, in the `Cookie` header, with every later request to the same site, as long as the cookie's attributes permit it.

The attributes of a cookie control where it is sent and who can read it: `Domain` and `Path` (which requests carry it), `Max-Age` or `Expires` (lifetime), `Secure` (only over HTTPS), `HttpOnly` (not readable by JavaScript, which protects it from theft by XSS, §7.5.2) and `SameSite` (whether it is sent with requests initiated by other sites, §7.5.4).

**Definition 7.4.3 (Session)** A server-side **session** is a record of the state of one user's interaction kept by the server (in a database, a cache or memory), identified by a long random *session ID*. The server gives the session ID to the browser in a cookie after a successful login, and on each request finds the session, and with it the user, by the ID in the cookie.

```mermaid
sequenceDiagram
  participant B as Browser
  participant S as Server
  participant DB as Session store
  B->>S: POST /login (username, password)
  S->>S: Verify the password hash
  S->>DB: Create session {user: 42}, ID = 9f3c...
  S-->>B: 200 OK, Set-Cookie: sessionid=9f3c...; HttpOnly; Secure; SameSite=Lax
  B->>S: GET /api/messages/ (Cookie: sessionid=9f3c...)
  S->>DB: Look up 9f3c...
  DB-->>S: user 42
  S-->>B: 200 OK, data for user 42
  B->>S: POST /logout
  S->>DB: Delete session 9f3c...
```

Sessions are simple and secure by default: the browser handles the cookie, an `HttpOnly` cookie is out of reach of scripts, and logging out (or revoking all sessions of a user whose password was stolen) is a deletion on the server. Their costs are a lookup in the session store on every request, a session store shared by all replicas of the back end, and cookies' awkwardness across sites and outside browsers: a cookie is sent automatically only to the site that set it, and cross-origin requests must opt in to sending it (`credentials: "include"` in `fetch`, plus the server's CORS permission).

### 7.4.3. Tokens and JWT

The alternative is to give the client a token that it presents explicitly.

**Definition 7.4.4 (Bearer Token)** A **bearer token** is a credential that grants access to whoever presents it, with no further proof of identity. The client sends it explicitly with each request, conventionally in the header `Authorization: Bearer <token>` (RFC 6750).

A token can be *opaque*, a random string that the server looks up in its database (as Django REST framework's `TokenAuthentication`, which uses the scheme name `Token` instead of `Bearer`), or *self-contained*, carrying the user's identity in a signed form that the server can verify without any lookup. The standard self-contained token is the JWT.

**Definition 7.4.5 (JSON Web Token)** A **JSON Web Token** (JWT, RFC 7519) is a compact string `header.payload.signature` of three Base64url-encoded parts: a *header*, a JSON object naming the signature algorithm (`"alg": "HS256"`) and type; a *payload*, a JSON object of *claims* about the subject, such as `sub` (subject, the user ID), `exp` (expiration time, in seconds since 1970) and `iat` (issued at); and a *signature* over the first two parts, computed with a key known only to the issuer (an HMAC with a shared secret for `HS256`, or a private key for `RS256` and `ES256`).

The following Python program, using only the standard library, issues a token, reads it as anyone can, verifies it as the server does, and rejects a forged and an expired token:

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

The output makes the essential properties visible.

- A JWT is signed, not encrypted: Base64url is an encoding, and anyone holding the token can read the payload. Never put secrets (passwords, personal data the client should not see) in it. (Encrypted tokens exist, JWE, but are rarely needed.)
- Nobody without the key can produce a valid token: changing the payload invalidates the signature. The comparison uses `hmac.compare_digest`, whose running time does not depend on where the strings differ, so that an attacker cannot guess the signature byte by byte from timings.
- The server must fix the accepted algorithm itself instead of trusting the header: libraries that honored `"alg": "none"` or let an attacker switch from `RS256` to `HS256` (using the public key as the HMAC secret) caused real vulnerabilities. In practice use a maintained library (PyJWT, `djangorestframework-simplejwt`, `jose` in JavaScript) rather than code like the above.
- Verification needs no database, which suits stateless replicas and microservices ([4.14.6](/4.14.6#sec-6.3.3)); but for the same reason a JWT cannot be revoked before it expires, unless the server keeps a deny list, which brings the lookup back.

The usual compromise is a pair of tokens: a short-lived *access token* (minutes) that authorizes API requests, and a long-lived *refresh token*, kept more carefully and checked against the database, with which the client obtains new access tokens; revoking the refresh token logs the user out within minutes. Where the browser should store tokens is a trade-off of its own: JavaScript-readable storage (`localStorage`) is exposed to any XSS on the site, while an `HttpOnly` cookie is not readable by scripts but brings back CSRF (§7.5.4). For a browser front end served from the same site as its API, a session cookie is usually the simpler and safer choice; tokens fit mobile apps, command-line clients, third-party API access and service-to-service calls.

### 7.4.4. Sessions versus Tokens, and OAuth

| | Session cookie | Opaque bearer token | JWT |
|---|---|---|---|
| where state lives | server (session store) | server (token table) | in the token |
| sent by | browser, automatically | client code, explicitly | client code, explicitly |
| lookup per request | yes | yes | no (signature check) |
| revocation | delete the session | delete the token | wait for expiry, or a deny list |
| exposure to XSS | low with `HttpOnly` | high if in `localStorage` | high if in `localStorage` |
| exposure to CSRF | yes, needs protection | no | no |
| suited to | browser apps on one site | API clients, scripts | distributed services, federated login |

Signing in "with" another account (a university account, GitHub, Google) uses *OAuth 2.0* (RFC 6749, consolidated in the OAuth 2.1 draft), an authorization framework in which a user lets an application obtain an access token from an authorization server without giving the application their password, and *OpenID Connect*, a layer on top of it that also returns a signed ID token (a JWT) stating who the user is. The flow for web and mobile apps is the *authorization code flow with PKCE*:

```mermaid
sequenceDiagram
  actor U as User
  participant B as Browser
  participant App as Application back end
  participant AS as Authorization server
  U->>B: Click "Log in with university account"
  B->>AS: Redirect: /authorize?client_id, redirect_uri, scope, state, code_challenge
  AS->>U: Login page and consent
  U->>AS: Credentials (entered at the authorization server only)
  AS-->>B: Redirect to redirect_uri?code=...&state=...
  B->>App: GET /callback?code=...&state=...
  App->>AS: POST /token (code, code_verifier, client secret)
  AS-->>App: access token, ID token (JWT)
  App->>App: Verify the ID token, create a session
  App-->>B: Set-Cookie: sessionid=...
```

The `state` parameter ties the callback to the request the application made (against CSRF on the login itself), and PKCE (a random `code_verifier` whose hash was sent as `code_challenge`) ensures that an intercepted code is useless to anyone else.

## 7.5. Security

Security problems in web applications are not exotic: the same few mistakes account for most incidents, and every one of them must be designed against from the start.

### 7.5.1. Never Trust the Client

The front end runs on the user's machine and is entirely under the user's control: its source can be modified, the browser's developer tools can change any request, and a script can call the API directly without any front end. However strict the checks in the front end are, the back end must treat every request as possibly crafted. Otherwise a user can:

- order $-10$ items, or change the price of an item to $-100$ in the request body;
- give a product a rating of $-2147483648$ stars, the smallest 32-bit integer, which the server may turn into a nonsensical or overflowing average (**integer overflow**);
- set fields that the form does not show, such as `"author": "bob"` or `"is_admin": true` (*mass assignment*), which is why the message board takes the author from the authenticated user and ignores the field in the body;
- access other users' objects by changing an ID in the URL (§7.4.1).

Validation in the front end exists for the user's convenience (immediate feedback, no wasted round trip); validation in the back end exists for correctness and security. The back end checks types, ranges, lengths, formats, ownership and business rules on every request, with an allowlist of accepted fields, and treats anything else as an error. CORS and CSRF protection (below) do not change this: they protect users' browsers, not the API, and nothing prevents anyone from calling the API with a Python script.

### 7.5.2. Injection and Cross-Site Scripting

Untrusted input becomes dangerous when it reaches an interpreter as code instead of data. The comment `Wow <script>alert("XSS")</script>`, if inserted unescaped into a page, runs as a script in every visitor's browser; a file `shell.php` containing `<?php system($_GET["cmd"]); ?>`, if uploaded into a directory that the web server executes, gives the attacker a shell on the server; a request `/user?id=1%3B%20DROP%20DATABASE%3B` (the decoded parameter is `1; DROP DATABASE;`), if pasted into an SQL string, may destroy the database. The last is SQL injection, treated with its defense, the parameterized query, in [4.13.4](/4.13.4#sec-4.9.2). The general rule is the same for every interpreter: keep code and data apart by passing data through an interface that cannot interpret it (query parameters, argument lists for `subprocess` instead of a **shell** command string, templating that escapes), and never build code by string concatenation.

**Definition 7.5.1 (Cross-Site Scripting)** **Cross-site scripting** (XSS) is an injection attack in which an attacker causes a web page to include script that the victim's browser executes in the context of the page's site, with access to its data, cookies not marked `HttpOnly`, tokens in storage and the ability to send requests as the user. In *stored* XSS the script is saved on the server (in a comment) and served to every visitor; in *reflected* XSS it travels in a request parameter that the server echoes into the response; in *DOM-based* XSS front-end code inserts untrusted data into the page itself.

The defenses are layered. Escape output by context: modern templating engines (Django templates) and front-end frameworks (React, [4.14.8](/4.14.8#sec-8.2.2)) escape text by default, so the danger lies in their explicit escape hatches (`|safe`, `mark_safe`, `dangerouslySetInnerHTML`, `innerHTML`); rich text that must contain HTML is passed through a sanitizer such as DOMPurify. Add a *Content Security Policy* header that tells the browser which script sources are allowed (Django 6 has built-in CSP support), so that injected inline scripts do not run. Keep session cookies `HttpOnly`. For uploads, check type and size, store files outside the executable web root under generated names, and serve them with a fixed `Content-Type` (and `X-Content-Type-Options: nosniff`, which Django sets by default).

### 7.5.3. The Same-Origin Policy and CORS

**Definition 7.5.2 (Same-Origin Policy)** The **origin** of a web resource is the triple of scheme, host and port of its URL: `https://app.example.com` and `https://api.example.com:443` are different origins, as are `http://localhost:5173` and `http://localhost:8000`. The **same-origin policy** of browsers restricts how a document or script loaded from one origin can interact with resources from another: in particular, a script may send requests to another origin, but may not read the responses unless that origin permits it.

Without the policy, any web page you visit could use your logged-in browser to read your mail from another tab's site. A separated application whose front end and API are at different origins, however, needs a controlled exception.

**Definition 7.5.3 (Cross-Origin Resource Sharing)** **Cross-origin resource sharing** (CORS) is the protocol by which a server tells browsers which other origins may read its responses. The server answers with headers such as `Access-Control-Allow-Origin: https://app.example.com`. For requests that a plain HTML form could not send (methods other than `GET`, `HEAD` and `POST`, custom headers such as `Authorization`, or a JSON content type), the browser first sends a *preflight* request with method `OPTIONS`, and sends the actual request only if the server's answer allows the method, headers and origin.

A preflight from a front end at `http://localhost:5173` to the message board's back end, which has no CORS configuration, receives a normal `200` from Django REST framework, but without any `Access-Control-Allow-Origin` header; the browser therefore refuses to send the `POST` and reports a CORS error in the console:

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

There are two correct remedies. Configure CORS on the server for exactly the front end's origins (in Django with the package `django-cors-headers`: `CORS_ALLOWED_ORIGINS = ["https://app.example.com"]`); never reflect any `Origin` back, and never combine a wildcard with credentials. Or avoid cross-origin requests altogether by serving front end and API from one origin through a reverse proxy (§7.2.2). Three misunderstandings are common. CORS is a relaxation of the same-origin policy, not a protection of the server: a missing CORS header does not stop "simple" requests from being sent and executed, only their responses from being read. It is enforced only by browsers, so it does nothing against scripts and other clients. And serving everything from one origin does not make cross-site attacks impossible: CSRF still has to be handled.

### 7.5.4. Cross-Site Request Forgery

**Definition 7.5.4 (Cross-Site Request Forgery)** **Cross-site request forgery** (CSRF) is an attack in which a malicious site causes the victim's browser to send a state-changing request to another site where the victim is logged in; because the browser attaches that site's cookies automatically, the request is executed with the victim's authority, although the victim never intended it.

A page on `evil.example` that contains a hidden form posting to `https://bank.example/transfer` and submits it with a line of JavaScript is enough, if the bank authenticates by cookie and does nothing else. The attacker cannot read the response (the same-origin policy), but does not need to. The defenses:

- `SameSite` cookies: with `SameSite=Lax` (Chromium-based browsers apply it to cookies that set no `SameSite` attribute; set it explicitly) the cookie is not sent with cross-site `POST` requests, and with `Strict` not even with cross-site links;
- an anti-CSRF token: the server puts a secret value into each form or into a cookie that the page's JavaScript copies into a header (Django's `csrftoken` cookie and `X-CSRFToken` header), and rejects state-changing requests without it, which another site cannot obtain;
- checking the `Origin` (or `Referer`) header of state-changing requests against an allowlist, which Django also does;
- keeping `GET` safe (§7.1.2), since links and images trigger `GET` requests from anywhere.

Django's `CsrfViewMiddleware` is enabled by default and rejected a JSON `POST` to a plain Django view in the message board project with `403 Forbidden` and the log line `Forbidden (CSRF cookie not set.)`, which is the protection working, not a bug to be fixed with `@csrf_exempt`. APIs authenticated only by an explicit `Authorization` header are not exposed to CSRF, because browsers never add that header on their own; this is why Django REST framework enforces CSRF only for session-authenticated requests.

### 7.5.5. A Checklist

The OWASP Top 10 (2025 edition) ranks the most critical risks to web applications by data from real incidents: broken access control, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, security logging and alerting failures, and mishandling of exceptional conditions. OWASP's cheat sheets give concrete guidance for each. A minimal checklist for the applications of this course:

| Area | Practice |
|---|---|
| transport | HTTPS everywhere; HSTS; `Secure` cookies |
| input | validate every field on the server against an allowlist; limit sizes |
| access control | check authentication and object-level authorization in every view; deny by default |
| injection | parameterized queries or an ORM; no shell strings; no `eval` |
| output | rely on auto-escaping; sanitize HTML; Content Security Policy |
| sessions and tokens | `HttpOnly`, `SameSite` cookies; short-lived tokens; never secrets in a JWT payload |
| cross-site | CORS only for known origins; CSRF protection for cookie-based authentication |
| secrets | keys and passwords in environment variables or a secret store, never in Git |
| configuration | `DEBUG` off in production; no default credentials; error pages without stack traces |
| dependencies | lock versions, update regularly, scan for known vulnerabilities |
| logging | log authentication failures and access denials, never passwords or tokens |
| abuse | rate limiting on login and expensive endpoints |

## 7.6. Separation When Agents Write the Code

Separation fits work with **coding agents** well, provided the contract comes first. An OpenAPI description or a set of shared types is a precise, machine-checkable specification ([4.14.4](/4.14.4#sec-4.6)) that lets one agent implement the back end and another the front end in parallel without touching each other's files, each against a mock of the other side; a contract test that validates real responses against the schema then catches drift between them. Security deserves a reviewer's particular attention, because generated code tends to make exactly the mistakes of §7.5: it checks that a user is logged in but not that the object is theirs, copies all request fields into the model, disables CSRF or allows every CORS origin to make an error message go away, and logs tokens while debugging. Negative tests (an anonymous `POST` must get `401`, another user's `DELETE` must get `403`, an oversized field must get `400`), written or reviewed by a human before the implementation, turn these requirements into checks that the agent cannot argue with ([4.14.9](/4.14.9#sec-9.7.2)).

## Summary

- HTTP is a stateless request–response protocol: method, target, headers and body; status code, headers and body. `GET`, `HEAD`, `OPTIONS` are safe; `PUT` and `DELETE` are idempotent, `POST` is not. `4xx` codes blame the request, `5xx` the server; `401` means unauthenticated, `403` forbidden.
- Server-side rendering builds HTML per request; a single-page application loads once and fetches JSON. Front-end/back-end separation splits the client program and the API server, which pays off with several clients, rich interaction, separate teams and scaling, and costs an API contract and two deployments.
- Separated systems are deployed either at two origins (with CORS) or behind a reverse proxy at one origin; static files go to a CDN, stateless back-end replicas behind a load balancer.
- Design the API first, from the clients' needs; write it down as OpenAPI or shared types. Use REST-style resources, JSON with explicit conventions for dates, money and IDs, meaningful status codes with structured error bodies (RFC 9457), pagination and compatible evolution.
- Authentication establishes identity, authorization decides access, for every object. Sessions keep state on the server and use cookies; bearer tokens are sent explicitly; JWTs are signed (readable, not secret) and verified without a lookup but hard to revoke. OAuth 2.0 with OpenID Connect delegates login.
- Never trust the client. Prevent injection by keeping code and data apart, XSS by escaping and CSP, cross-origin reading by the same-origin policy with narrow CORS rules, and CSRF by `SameSite` cookies, CSRF tokens and origin checks.

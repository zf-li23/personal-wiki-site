# 即时通讯系统 Markdown 功能展示

## 一、基础文本格式

**粗体文本** - 用于强调关键信息
*斜体文本* - 用于引用或注释
~~删除线文本~~ - 用于标记已取消内容
`行内代码` - 用于技术术语或命令

**组合效果**：这是一个*非常*~~简单~~ **重要**的`system.out.println("示例")`

## 二、标题层级结构

# 一级标题 (H1)
## 二级标题 (H2)
### 三级标题 (H3)
#### 四级标题 (H4)

## 三、列表展示

### 无序列表
- ✅ 已实现文本消息
- 🔄 正在开发文件传输
- 📅 计划中的视频通话
- ✨ **高级功能**
  - 消息撤回
  - 已读回执
  - 消息回复链

### 有序列表
1. **第一步：用户注册**
   - 邮箱验证
   - 密码强度检查
2. **第二步：添加好友**
   - 搜索用户名
   - 发送好友请求
3. **第三步：开始聊天**
   - 创建会话
   - 发送第一条消息

## 四、代码与数学公式

### Python代码块
```python
def calculate_fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

# 测试代码
result = calculate_fibonacci(10)
print(f"斐波那契数列第10项: {result}")
```

### JavaScript代码块
```javascript
// WebSocket连接示例
const socket = new WebSocket('wss://im-server.example.com');

socket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    console.log('收到消息:', message);
    
    // 更新UI
    if (message.type === 'text') {
        displayMessage(message.content);
    }
};
```

### 数学公式（LaTeX）
线性回归方程：
$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \epsilon
$$

贝叶斯定理：
$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

欧拉公式（数学中最美的公式之一）：
$$
e^{i\pi} + 1 = 0
$$

### 新增数学公式测试

**行内公式测试：**
这是一个行内公式 $E=mc^2$ 使用单美元符号。
这是另一个行内公式 \( a^2 + b^2 = c^2 \) 使用斜杠括号。

**行间公式测试：**
使用双美元符号：
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

使用斜杠中括号：
\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]

### 代码样式测试

行内代码测试：`const a = "hello"` 应该有灰色背景且无引号。

代码块复制测试：
```typescript
console.log("Try copying this!");
```


## 五、表格数据展示

### 项目进度表
| 功能模块 | 负责人 | 进度 | 预计完成 |
|---------|--------|------|----------|
| 用户认证 | 张三 | ✅ 100% | 2024-03-01 |
| 好友系统 | 李四 | 🔄 85% | 2024-03-10 |
| 群聊功能 | 王五 | 🔄 90% | 2024-03-08 |
| 文件传输 | 赵六 | 🔄 70% | 2024-03-15 |
| 消息推送 | 钱七 | 🔄 95% | 2024-03-05 |

### 性能数据对比
| 消息类型 | 平均延迟 | 成功率 | 大小限制 |
|----------|----------|--------|----------|
| 文本消息 | 128ms | 99.9% | 64KB |
| 图片消息 | 256ms | 99.5% | 10MB |
| 语音消息 | 312ms | 99.2% | 20MB |
| 视频消息 | 480ms | 98.8% | 100MB |
| 文件传输 | 可变 | 99.0% | 1GB |

## 六、引用与备注

> **爱因斯坦说过：**  
> "Logic will get you from A to B. Imagination will take you everywhere."
> 
> *这提醒我们，技术实现需要逻辑，但好的产品需要想象力。*

### 注意事项
1. **安全提醒**：
   > 所有消息都经过端到端加密，确保通信安全。

2. **使用建议**：
   > Markdown语法在发送前会实时预览，帮助用户确认格式。

## 七、任务列表

- [x] 完成Markdown解析器
- [x] 实现代码高亮
- [x] 支持LaTeX数学公式
- [ ] 添加更多主题样式
- [ ] 实现Markdown导入/导出
- [ ] 开发移动端优化

## 八、特殊格式示例

### 键盘快捷键
使用 **`Ctrl + B`** 快速加粗，**`Ctrl + I`** 快速斜体

### 进度表示
项目完成度：`██████████ 90%`  
代码覆盖率：`████████░░ 80%`

### 对比展示
**优化前：**
```plaintext
用户A：这个函数的参数应该怎么传？
用户B：看文档第23页
用户A：文档里没写清楚
```

**优化后（使用Markdown）：**
```markdown
用户A：`calculate_fibonacci()`函数的`n`参数应该传什么类型？

用户B：
```python
# 应该是整数类型，且n >= 0
result = calculate_fibonacci(10)  # ✅ 正确
result = calculate_fibonacci(-1)  # ❌ 错误
```


---

## 九、图片嵌入示例

### 系统架构图

![系统架构示意图](https://img-s.msn.cn/tenant/amp/entityid/AA1ToHUJ.img?w=768&h=512&m=6&x=451&y=76&s=50&d=50)

### 用户界面预览

![聊天界面](https://via.placeholder.com/400x300/7ED321/FFFFFF?text=Chat+Interface+Preview)
*图：我们的聊天界面支持Markdown实时渲染*

---

## 十、综合示例：技术文档片段

### **功能：消息撤回机制**
**实现原理：**
```python
class MessageManager:
    def recall_message(self, message_id, user_id):
        """撤回指定消息"""
        # 1. 验证权限
        if not self.can_recall(message_id, user_id):
            raise PermissionError("无权撤回此消息")
        
        # 2. 更新消息状态
        self.update_message_status(message_id, "recalled")
        
        # 3. 通知所有在线用户
        self.broadcast_recall(message_id)
        
        return {"status": "success", "message": "消息已撤回"}
```

**状态流转：**
| 状态 | 描述 | 可执行操作 |
|------|------|------------|
| `sent` | 已发送 | 撤回、回复、转发 |
| `delivered` | 已送达 | 撤回、回复、转发 |
| `read` | 已读 | 撤回（限2分钟内） |
| `recalled` | 已撤回 | 查看撤回提示 |

**数学约束：**
撤回时间限制公式：
$$
t_{\text{撤回}} \leq t_{\text{发送}} + 120\text{s}
$$

---

**总结：** 我们的Markdown引擎支持完整的CommonMark标准，并扩展了数学公式、任务列表、复杂表格等高级功能，为技术团队提供了极致的沟通体验。

> *提示：以上所有内容均在我们的即时通讯系统中完全支持，并可以实时预览和渲染。*
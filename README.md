# 1. 视图拆分
## 1.1 使用 Blueprint
Blueprint 用于模块级拆分，不适合用于视图拆分。
Blueprint 用于视图拆分的缺陷：
1. 路由重复：api 每个视图前面的部分路由都是一样的，可提取出来作为前缀。

在以上分析的基础上设计 Redprint，用于视图级拆分。
## 1.2 Redprint
### 1.2.1 初始化
### 1.2.2 route
### 1.2.3 提取重复路由作为前缀
### 1.2.4 注册到 Blueprint
# 2. REST
REST 把服务器所有数据都视为资源。
## 2.1 使用URL来定位资源
URL 不应该包含动词，只是用来定位资源的。
## 2.2 使用HTTP动词来操作资源
GET、POST、PUT、DELETE
## 2.3 REST 适用场景
1. REST 适用于开放 API，对于内部开发不适用，因为标准 REST 有 CURD 四种操作，不一定能够承载业务。
2. 接口粒度比较粗，前端开发不方便。
3. REST 一个接口只返回一个资源，当需要返回多个有关联资源时，无法一次性全部返回，只能发送多个请求依次取得数据，造成 HTTP 请求的数量大幅增加。

**总结：**
尽量遵守 REST 设计风格，但不死板盲从，根据业务逻辑灵活调整。
## 2.4 REST细节特性
### 2.4.1 输入/输出都需要是json格式
### 2.4.2 HTTP状态码都是有意义的
2xx, 3xx, 4xx, 5xx
### 2.4.3 返回信息分类
1. 业务数据信息。
2. 操作成功提示信息。
3. **错误异常信息**，决定API的优劣程度，如果返回的错误异常信息不够标准，客户端很难处理错误。
```
{
    "msg": "xxx", // 错误异常信息
    "error_code": 1000, // 错误码
    "request": url // 当前的http请求url路径
}
```
# 3. 异常处理
## 3.1 已知异常
我们可以预知的异常。
**解决办法**：抛出APIException。
## 3.2 未知异常
我们没有意识到的异常，如何统一数据的返回格式？即json格式。

**解决办法**：在全局的某个地方捕获到所有未知异常，统一处理未知异常——AOP思想。
将未知异常分为两种：HTTPException/Exception。分别代表HTTP错误和服务器代码错误，最后都包装成APIException抛出。
# 4. Token
用户有效身份的凭据。
## 4.1 三个特征
1. 有效期，一般为2小时。
2. 标识用户的身份，存储用户ID号。
3. Token是加密的。
## 4.2 Token有什么用
### 4.2.1 保护接口（auth拦截器）
只有登录的用户，才可访问某些接口，而是否可访问的校验通过Token实现。
访问接口时若令牌**没有过期**，而且**合法**，那么可以通过接口进行正确操作。
## 4.3 Token如何使用
1. 可自定义传入账号和密码，但HTTP协议本身就规定了一种传递账号和密码的方法。
将账号和密码放入header中发送：
```
key=Authorization
value=basic base64(account:password)
```
2. 将Token当作account发送，password不传任何数据。
## 4.4 验证Token的代码应该写在什么地方？
利用装饰器，哪个接口需要Token验证，就在哪个接口上方加入装饰器。

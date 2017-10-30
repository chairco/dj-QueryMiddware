## HTTP回傳狀態碼

API回傳的結果，應使用適當的HTTP狀態碼，所以API設計者必須了解它們。以下是一些常用的狀態碼，完整列表請參考Wikipedia。


### 2xx: 成功
+ 200 OK: 通用狀態碼
+ 201 Created: 資源新增成功
+ 202 Accepted: 請求已接受，但尚在處理中
+ 204 No Content: 請求成功，但未回傳任何內容


### 3xx: 重新導向
+ 301 Moved Permanently: 資源已移至它處
+ 303 See Other: 回傳的內容可在它處取得（例如在用戶端發送了一個POST請求之後）
+ 304 Not Modified: 請求的資源並未修改（通常是用戶端發送了帶有If-Modified-Since或If-None-Match表頭的請求）


### 4xx: 用戶端錯誤（用戶端不應retry原始請求）
+ 400 Bad Request: 通用狀態碼
+ 401 Unauthorized: 用戶端尚未驗證*
+ 403 Forbidden: 用戶端被禁止此請求*
+ 404 Not Found: 請求的資源不存在
+ 405 Method Not Allowed: 不支援請求的HTTP方法
+ 406 Not Acceptable: 不支援請求所要求的內容類型（Accept表頭）
+ 415 Unsupported Media Type: 不支援請求所用的內容類型（Content-Type表頭）


### 5xx: 伺服器錯誤（用戶端可合理retry）
+ 500 Internal Server Error: 工程師要找bug了
+ 501 Not Implemented: 用戶端的請求目前未支援（也就是將來有可能支援）
+ 502 Bad Gateway: 上游的伺服器未回傳正確結果，一般是gateway或proxy server才會回傳此狀態碼
+ 503 Service Unavailable: 暫停服務（也就是過不久就會恢復服務──如果一切順利的話）
+ 504 Gateway Timeout: 上游的伺服器逾時，一般是gateway或proxy server才會回傳此狀態碼
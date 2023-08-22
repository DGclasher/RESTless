# RESTless API Docs

## Fetch Quotes and Authors

### Fetch Quote

<details>
 <summary><code>GET</code> <code>/api/fetch/quote/</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                          |
> |---------------|-----------------------------------|-----------------------------------|
> | `200`         | `application/json`                | JSON                              |

##### Example cURL

> ```javascript
>  curl "https://resttless.vercel.app/api/fetch/quote/?format=json"
> ```

</details>

### Fetch Author by Name or ID

<details>
 <summary><code>GET</code> <code>/api/fetch/author</code><code><b>/{author name or id}</b></code> </summary>

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `name` or `id`    | required  | string / int   | Author's name or ID                 |

##### Responses

> | http code     | content-type                      | response                         |
> |---------------|-----------------------------------|----------------------------------|
> | `200`         | `application/json`                | JSON                             |

##### Example cURL
##### For name
> ```javascript
>  curl "https://resttless.vercel.app/api/fetch/author/?name=Thomas+Edison&format=json"
> ```

#### For ID
> ```javascript
>  curl "https://resttless.vercel.app/api/fetch/author/?id=5&format=json"
> ```

</details>

### Fetch all Authors

<details>
    <summary><code>GET</code> <code>/api/fetch/author</code></summary>

##### Parameters
> None

##### Responses
> | http code     | content-type                      | response                         |
> |---------------|-----------------------------------|----------------------------------|
> | `200`         | `application/json`                | JSON                             |

##### Example cURL
> ```javascript
>  curl "https://resttless.vercel.app/api/fetch/author/all/?format=json"
> ```
</details>

------------------------------------------------------------------------------------------------

## Create Quotes and Authors

### Create Author

<details>
 <summary><code>POST</code> <code>/api/create/author/</code></summary>

##### Parameters

> None

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://resttless.vercel.app/users/my_account"> here </a> |


##### Data

> | name      |  type     | data type               | description                       |
> |-----------|-----------|-------------------------|-----------------------------------|
> | `name`    |  required | JSON                    | Specify the name of the author to be created |


##### Responses

> | http code     | content-type                      | response                                            |
> |---------------|-----------------------------------|-----------------------------------------------------|
> | `201`         | `application/json`                | `{id: [author_id], name: [author_name]}`            |
> | `405`         | `application/json`                | `{'detail': 'Method "<method_name>" not allowed.'}` |

##### Example cURL

> ```javascript
>  curl -X POST -H "Authorization: Token < your_auth_token >" -H "Content-Type: application/json" -d '{"name" : "Lucas"}' "https://resttless.vercel.app/api/create/author/"
> ```

</details>

### Create Quote

<details>
 <summary><code>POST</code> <code>/api/create/quote/</code></summary>

##### Parameters

> None

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://resttless.vercel.app/users/my_account"> here </a> |


##### Data

> | name      |  type     | data type               | description                       |
> |-----------|-----------|-------------------------|-----------------------------------|
> | `name`    |  required | JSON                    | Specify the name of the author    |
> | `quote`   |  required | JSON                    | Quote to post                     |
> | `author_id` | required | JSON                   | ID of author                      |


##### Responses

> | http code     | content-type                      | response                                            |
> |---------------|-----------------------------------|-----------------------------------------------------|
> | `201`         | `application/json`                | `{'quote': '<quote>', 'author_id': <author id>, 'author': {'id': <author id>, 'name': '<author name>'}}`            |
> | `405`         | `application/json`                | `{'detail': 'Method "<method_name>" not allowed.'}` |

##### Example cURL

> ```javascript
>  curl -X POST -H "Authorization: Token < your_auth_token >" -H "Content-Type: application/json" -d "{'quote': 'doing from client', 'author_id': 14, 'author': {'id': 14, 'name': 'unknown'}}" "https://resttless.vercel.app/api/create/quote/"
> ```

</details>

------------------------------------------------------------------------------------------------

## Update Author

### Update Author

<details>
 <summary><code>PUT</code> <code>/api/update/author/</code></summary>

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              | required  |   int          | Author's ID                         |

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://resttless.vercel.app/users/my_account"> here </a> |


##### Data

> | name      |  type     | data type               | description                       |
> |-----------|-----------|-------------------------|-----------------------------------|
> | `name`    |  required | JSON                    | New name of Author               |


##### Responses

> | http code     | content-type                      | response                                            |
> |---------------|-----------------------------------|-----------------------------------------------------|
> | `200`         | `application/json`                | `{'message':'author updated'}` || `{'message':'Not allowed on that author'}`                      |
> | `405`         | `application/json`                | `{'detail': 'Method "<method_name>" not allowed.'}` |

##### Example cURL

> ```javascript
>  curl -X PUT -H "Authorization: Token < your_auth_token >" -H "Content-Type: application/json" -d '{"name" : "Lucas"}' "https://resttless.vercel.app/api/update/author/100"
> ```

</details>

------------------------------------------------------------------------------------------------

## Delete Quote and Author

### Delete Author

<details>
 <summary><code>DELETE</code> <code>/api/delete/author/</code></summary>

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              | required  |   int          | Author's ID                         |

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://resttless.vercel.app/users/my_account"> here </a> |


##### Data

> None


##### Responses

> | http code     | content-type                      | response                                            |
> |---------------|-----------------------------------|-----------------------------------------------------|
> | `200`         | `application/json`                | `{'message':'author deleted'}` || `{'message':'Not allowed on that author'}`                      |
> | `405`         | `application/json`                | `{'detail': 'Method "<method_name>" not allowed.'}` |

##### Example cURL

> ```javascript
>  curl -X DELETE -H "Authorization: Token < your_auth_token >" "https://resttless.vercel.app/api/delete/author/100"
> ```

</details>

### Delete Quote

<details>
 <summary><code>DELETE</code> <code>/api/delete/quote/</code></summary>

##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              | required  |   int          | Quote ID                         |

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://resttless.vercel.app/users/my_account"> here </a> |


##### Data

> None


##### Responses

> | http code     | content-type                      | response                                            |
> |---------------|-----------------------------------|-----------------------------------------------------|
> | `200`         | `application/json`                | `{'message':'Quote Deleted'}` || `{'message':'Not allowed on that quote'}`                      |
> | `405`         | `application/json`                | `{'detail': 'Method "<method_name>" not allowed.'}` |

##### Example cURL

> ```javascript
>  curl -X DELETE -H "Authorization: Token < your_auth_token >" "https://resttless.vercel.app/api/delete/quote/120"
> ```

</details>
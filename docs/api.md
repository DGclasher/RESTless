# RESTless API Docs
------------------------------------------------------------------------------------------

## Fetch Quotes and Authors

### Fetch Quote

<details>
 <summary><code>GET </code><code>/api/fetch/quote/</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                          |
> |---------------|-----------------------------------|-----------------------------------|
> | `200`         | `application/json`                | JSON                              |

##### Example cURL

> ```javascript
>  curl "https://restless.pythonanywhere.com/api/fetch/quote/?format=json"
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
>  curl "http://restless.pythonanywhere.com/api/fetch/author/?name=Thomas+Edison&format=json"
> ```

#### For ID
> ```javascript
>  curl "http://restless.pythonanywhere.com/api/fetch/author/?id=5&format=json"
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
>  curl "http://restless.pythonanywhere.com/api/fetch/author/all/?format=json"
> ```
</details>

------------------------------------------------------------------------------------------------

## Create Quotes and Authors

### Create Author

<details>
 <summary><code>POST </code><code>/api/create/author/</code></summary>

##### Parameters

> None

##### Headers

> | name            |  type     | data type               | description                       |
> |-----------------|-----------|-------------------------|-----------------------------------|
> | `Authorization` | required  |                         | Pass the authorization token, get it from <a href="https://restless.pythonanywhere.com/users/my_account"> here </a> |


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
>  curl -X POST -H "Authorization: Token < your_auth_token >" -H "Content-Type: application/json" -d '{"name" : "Lucas"}' "http://restless.pythonanywher.com/api/create/author/"
> ```

</details>


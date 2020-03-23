# Book Library registry

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all books

**Definition**

`GET /books`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "unique-bookId",
        "name": "Book Name",
        "author": "author name"
    },
    {
        "identifier": "brave_new",
        "name": "Brave New World",
        "author": "Aldous Huxley"
    }
]
```

### Adding a new book

**Definition**

`POST /books`

**Arguments**

- `"identifier":string` a globally unique identifier for this book
- `"name":string` the book name
- `"author":string` author name

If a book with the given identifier already exists, the existing book will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "identifier": "brave_new",
    "name": "Brave New World",
    "author": "Aldous Huxley"
}
```

## Lookup books details

`GET /book/<identifier>`

**Response**

- `404 Not Found` if the book does not exist
- `200 OK` on success

```json
{
    "identifier": "brave_new",
    "name": "Brave New World",
    "author": "Aldous Huxley"
}
```

## Delete a book

**Definition**

`DELETE /books/<identifier>`

**Response**

- `404 Not Found` if the book does not exist
- `204 No Content` on success

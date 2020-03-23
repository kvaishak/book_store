<html>
    <head>
        <title>Vaishaks Book Store</title>
    </head>
    <body>
        <h1> Welcome to your Book Store </h1>
        <ul>
            <?php
            $json = file_get_contents("http://book-library/books");
            $obj = json_decode($json);
            // echo "$json";
            $books = $obj->data;
            foreach ($books as $book) {
                echo "<li> $book->name : written by [$book->author] </li>";
            }
             ?>
        </ul>
    </body>
</html>

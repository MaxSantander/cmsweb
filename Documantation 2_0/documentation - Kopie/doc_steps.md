%! Author = maxu2
%! Date = 14.11.2024

% Preamble
\documentclass[11pt]{article}

% Packages
\usepackage{amsmath}
\usepackage{hyperref}
\usepackage{hyperref}

% Document
\begin{document}

    \section*{ PL/Python Functions \href{https://www.postgresql.org/docs/17/plpython-funcs.html#PLPYTHON-FUNCS}{}}

    Functions in PL/Python are declared via the standard \href{https://www.postgresql.org/docs/17/sql-createfunction.html}{CREATE FUNCTION} syntax:
    \newcommand{\plpythonlang}{LANGUAGE plpython3u}
    CREATE FUNCTION \textit{funcname} (\textit{argument-list})
    RETURNS \textit{return-type}
    AS $$
    # PL/Python function body
    $$ \plpythonlang;
    The body of a function is simply a Python script. When the function is called, its arguments are passed as elements of the list args; named arguments are also passed as ordinary variables to the Python script. Use of named arguments is usually more readable. The result is returned from the Python code in the usual way, with return or yield (in case of a result-set statement). If you do not provide a return value, Python returns the default None. PL/Python translates Python's None into the SQL null value. In a procedure, the result from the Python code must be None (typically achieved by ending the procedure without a return statement or by using a return statement without argument); otherwise, an error will be raised.

    For example, a function to return the greater of two integers can be defined as:
    CREATE FUNCTION get_max (num1 integer, num2 integer)
    RETURNS integer
    AS $$
    if num1 > num2:
    return num1
    return num2
    $$ \plpythonlang;
    The Python code that is given as the body of the function definition is transformed into a Python function. For example, the above results in:
    def __plpython_procedure_get_max_23456():
    if num1 > num2:
    return num1
    return num2
    assuming that 23456 is the OID assigned to the function by PostgreSQL.

    The arguments are set as global variables. Because of the scoping rules of Python, this has the subtle consequence that an argument variable cannot be reassigned inside the function to the value of an expression that involves the variable name itself, unless the variable is redeclared as global in the block. For example, the following won't work:
    CREATE FUNCTION strip_text(input_text text)
    RETURNS text
    AS $$
    input_text = input_text.strip()  # error
    return input_text
    $$ \plpythonlang;
    because assigning to input_text makes input_text a local variable for the entire block, and so the input_text on the right-hand side of the assignment refers to a not-yet-assigned local variable input_text, not the PL/Python function parameter. Using the global statement, this can be made to work:
    CREATE FUNCTION strip_text(input_text text)
    RETURNS text
    AS $$
    global input_text
    input_text = input_text.strip()  # ok now
    return input_text
    $$ \plpythonlang;
    But it is advisable not to rely on this implementation detail of PL/Python. It is better to treat the function parameters as read-only.


    openssl genrsa -des3 -out server.key 1024
    openssl rsa -in server.key -out server.key
    openssl req -new -key server.key -out server.csr
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt


    notepad "C:\Program Files\PostgreSQL\17\data\postgresql.conf"
    notepad "C:\Program Files\PostgreSQL\17\data\pg_hba.conf"


    net stop postgresql-x64-17
    net start postgresql-x64-17


CREATE USER ris_admin WITH PASSWORD 'ris2016!';


psql -U postgres -h localhost













    C:\Program Files\PostgreSQL\13\data postgresql.con


\end{document}
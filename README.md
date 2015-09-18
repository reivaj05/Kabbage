Twitter & Wikipedia results
===========

Simple Application to retrieve results from Twitter and Wikipedia passing a query as parameter

### Feature work

* Improvement and refactoring of code on results_search.html
* Add ‘limit results those near me’ option

### Requirements

* [Vagrant](https://www.vagrantup.com/downloads.html) 1.7.x or greater

### Set up development environment

* Run the following command to setup virtual environment
(it may take a while the first time)

```sh
vagrant up
```

* When the virtual environment is ready, establish a connection with the
following command

```sh
vagrant ssh
```

### Contributing

To ensure the project quality, you must run the following script before every
commit and make sure no problems were detected

```sh
sh tests.sh
```

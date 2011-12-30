## DjangoCMS Embedded Pages

This simple extension allows your admin users to embed other pages within
placeholders

## Requirements

* django-cms
* And all the requirements the above project(s) depend on.


## Installation

1. make sure you are using a python virtual environment

     virtualenv ~/Dev/virtualenv/projectname;
     . ~/Dev/virtualenv/projectname/bin/activate;
     cd ~/Dev/projects/projectname/;

2. install it from pypi

    `pip install cmsplugin-embedded-pages`

3. or, install it from github

    `pip install git+https://github.com/airtonix/cmsplugin-embedded-pages`


## Configuration

1. add `cmsplugin_embeddedpages` to `INSTALLED_APPS`

2. perform a `./manage.py migrate` (for south users), or `./manage.py syncdb`

3. There is no step three!


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

* cmsplugin_embeddedpages/layouts

Any .html file that doesn't contain the word 'default' will be presented in
the template selector combo dropdown in the admin interface.

For example, if your django project was at :

    ~/Dev/Django/MyProjectName/

And you had a django application named `SomethingSomethingSomething` at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/

Then templates for this plugin could be found at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_embeddedpages/layouts/*.html

In fact, anywhere django looks for templates, you can place the following tree :

    /cmsplugin_embeddedpages
        /layouts
            /*.html


### Customising Templates

Templates in all groups are provided the context :

a CMSPlugin has many useful attributes for you to use, the main one
is `plugin.instance` a reference to the settings model.

>     plugin' :
>         An instance of CMSPlugin, which itself provides reference to either
>         of the settings models as outlined below.

#### base.html

base.html in the `cmsplugin_configurableproduct` directory is used to load the
selected template chosen in the administration interface.


#### ./layouts/*.html

templates here are provided the context :

>     plugin.instance
>          template
>               Chosen template.
>
>     Pages
>        A list of cms.Page(s)




## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-embedded-pages


## Todo

provide option to manipulate menu choices:

* Refine the product filter.
* Provide better default templates.
* Allow selecting/use of snippets for menu templates?

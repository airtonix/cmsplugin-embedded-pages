## djangoCMS/Shop Configurable Products Extension

This simple extension provides some plugins to display things about your
[django-shop configurable products](https://bitbucket.org/zeus/django-shop-configurableproduct).


## Requirements

* django-shop
* django-cms
* django-shop-configurableproduct
* And all the requirements the above three projects depend on.


## Installation

1. make sure you are using a python virtual environment

    virtualenv ~/Dev/virtualenv/projectname
    . ~/Dev/virtualenv/projectname/bin/activate
    cd ~/Dev/projects/projectname/

2. install it from pypi

    pip install cmsplugin-configurableproduct

3. or, install it from github

    pip install git+https://github.com/airtonix/cmsplugin-configurableproduct


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

* cmsplugin_configurableproduct/product-types
* cmsplugin_configurableproduct/product-list

Any .html file that doesn't contain the word 'base' will be presented in
the template selector combo dropdown in the admin interface.

For example, if your django project was at :

    ~/Dev/Django/MyProjectName/

And you had a django application named `SomethingSomethingSomething` at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/

Then templates for this plugin could be found at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/product-types/*.html
    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/product-list/*.html

In fact, anywhere django looks for templates, you can place the following tree :

    /cmsplugin_configurableproduct
        /product-types
            /*.html
        /product-list
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


#### ./product-types/*.html

templates here are provided the context :

>     plugin.instance
>          categories
>               Chosen categories for this instance,
>
>          show_category_icon
>               For when configurable_product.ProductType stores an image.
>
>          hide_empty_categories
>               Self explanitory, effected in the cms_plugin.
>
>          template
>               Chosen template.
>
>     Types
>        A list of configurable_product.ProductType(s)


#### ./product-list/*.html

templates here are provided the context :


>     plugin.instance
>          categories
>               Chosen categories for this instance,
>
>          hide_empty_categories
>               Self explanitory, effected in the cms_plugin.
>
>          template
>               Chosen template.
>
>          filter_product_attributes
>               Comma separated list of CProductField names on which to
>               effect a filter action of either Filter, or Exclude.
>
>          filter_action
>               The action to take on the filter attributes listed above.
>
>     Products
>        A list of configurable_product.CProduct(s)



## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-configurableproduct


## Todo

provide option to manipulate menu choices:

* Refine the product filter.
* Provide better default templates.
* Allow selecting/use of snippets for menu templates?

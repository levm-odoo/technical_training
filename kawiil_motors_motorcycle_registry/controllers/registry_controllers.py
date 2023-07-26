from odoo import http

class Registry(http.Controller):
    ## -------------------
    ##  Registries routes
    ## -------------------
    # When using the 'website' arg makes posible for the function to access the website instead of being exclusively backend
    @http.route('/registry', auth='public', website=True)
    def index(self, **kw):
        return 'Hello World'
    
    @http.route('/registry/motorcycles', auth='public', website=True)
    def motorcycles(self, **kw):
        motorcycles = http.request.env['motorcycle.registry'].search([])
        return http.request.render('kawiil_motors_motorcycle_registry.registred_motorcycles_website', {
            'motorcycles':motorcycles
        })
    
    @http.route('/registry/<model("motorcycle.registry"):motorcycle>/', auth='public', website=True)
    def motorcycle(self, motorcycle):
        return http.request.render('kawiil_motors_motorcycle_registry.registred_motorcycle_website', {
            'motorcycle':motorcycle
        })
    
    ## -----------------------------
    ##  Motorcycles products routes
    ## -----------------------------
    @http.route('/compare', auth='public', website=True)
    def comparison(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','in',['motorcycle'])],[],[])
        return http.request.render('kawiil_motors_motorcycle_registry.compare_motorcycles_website', {
            'num_products':len(motorcycles),
            'motorcycles':motorcycles
        })
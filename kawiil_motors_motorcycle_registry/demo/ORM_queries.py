## ---------------------------------------
##  Interacción con el 'ambiente' del ORM
## ---------------------------------------
##   Utilizando la shell de Odoo se pueden realizar consultas rápidas e interactuar con registros de los modelos

env_reg = env['motorcycle.registry']

# 1. Creación de registro
new_reg = env_reg.create({
    'registry_number' : 'RN0004',
    'vin': 'VIM29375',
    'first_name' : 'Karla',
    'last_name' : 'Cuerso',
    'license_plate' : 'LI-GB9-02',
    'current_mileage' : 1320
})
# 2. Mileage menor igual a 1000
env_reg.read_group([('current_mileage','<=',1000)],[],['current_mileage'])
# 3. Registries with VIN but not License plate
env_reg.read_group([('vin','!=',False),('license_plate','=',False)],['registry_number','vin','license_plate','last_name'],['last_name'])
# 4.
env_reg.read_group(['|',('vin','!=',False),('license_plate','!=',False)],[],['last_name'])
# 5.
new_reg['first_name'] = 'Jhon'
new_reg['last_name'] = 'Wick'
# 6.
new_reg.unlink()
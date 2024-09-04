




def query_parametrs_filtering_generics(self,consider_list,Model_):
    from django.db.models import  Q 
    '''
    this function add some list field to set qury parameters 
    example:
            query_fields = ['brand','model',etc.....]
            return query_parametrs_filtering_generics(self,query_fields,LaptopProduct)
    in url http://127.0.0.1:5041/api/v1/showing_laptops/?brand=asus&series=rog
    it returns:
   {
        "id": 3,
        "brand": "asus",
        "model": "g16 g64jv",
        .....
    }
    '''
    
    filtering=Q() 
    for field in consider_list: 
        #?brand=lenovo
        value = self.request.query_params.get(field)  # self.request is the diffrence from @ and apiview #y700 #lenovo
        if value:  
            filtering &=(Q(**{field:value})) #(AND: ('brand', 'lenovo'), ('model', 'y700'))
    return  Model_.objects.filter(filtering) 




    
    
    
def requestsHelper(request):
    args = {}
    # print(request.args)
    # print(request.form)
    for arg in request.form:
        args[arg]=request.form.get(arg)
    return args
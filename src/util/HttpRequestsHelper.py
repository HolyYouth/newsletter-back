    
    
    
def requestsHelper(request):
    args = {}
    for arg in request.args:
        args[arg]=request.args.get(arg)
    return args
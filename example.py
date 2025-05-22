from argumentsignature import Argument, ArgumentValue, ARG, ARGS, KWARGS

def item_to_string(key1:str, key2:str, *keys:str, **items:int):
    itmes = [f'{k}:{v}' for k, v in items]
    return ", ".join([key1, key2, *keys, itmes])

arg_items = item_to_string.__annotations__.items()
code = item_to_string.__code__
arg_defaults = item_to_string.__kwdefaults__ or {}
names = code.co_varnames
arg_keys = names[:code.co_argcount]
kwarg_keys = list(arg_defaults.keys())
is_args = True

arguments:list[Argument] = []
for arg_name, arg_type in arg_items:
    if arg_name in arg_keys:
        arguments.append(Argument(
            name = arg_name,
            type = arg_type,
            argtype = ARG
        ))
    elif arg_name in kwarg_keys:
        arguments.append(Argument(
            name = arg_name, 
            type = arg_type, 
            default = arg_defaults[arg_name],
            argtype = ARG
        ))
    elif arg_name == 'return':
        continue
    else:
        arguments.append(Argument(
            name = arg_name,
            type = arg_type,
            argtype = ARGS if is_args else KWARGS
        ))
        is_args = False

print("\n\n".join([str(x) for x in arguments]))

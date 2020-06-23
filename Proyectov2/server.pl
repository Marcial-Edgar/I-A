:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_cors)).
:- use_module(library(pengines)).
:- http_handler(root(.),handle,[]).

server(Port) :- http_server(http_dispatch, [port(Port)]).

aplica(medio,medio,java,no,'Desarrollador Backend Jr').
aplica(medio,alto,java,no,'Desarrollador Backend Jr').
aplica(alto,alto,java,no,'Desarrollador Backend Jr').
aplica(medio,medio,csharp,no,'Desarrollador Backend Jr').
aplica(medio,alto,csharp,no,'Desarrollador Backend Jr').
aplica(alto,alto,csharp,no,'Desarrollador Backend Jr').
aplica(medio,medio,python,no,'Desarrollador Backend Jr').
aplica(medio,alto,python,no,'Desarrollador Backend Jr').
aplica(alto,alto,python,no,'Desarrollador Backend Jr').
aplica(medio,medio,php,no,'Desarrollador Backend Jr').
aplica(medio,alto,php,no,'Desarrollador Backend Jr').
aplica(alto,alto,php,no,'Desarrollador Backend Jr').
aplica(medio,medio,javascript,no,'Desarrollador Frontend Jr').
aplica(medio,alto,javascript,no,'Desarrollador Frontend Jr').
aplica(alto,alto,javascript,no,'Desarrollador Frontend Jr').
aplica(medio,medio,sql,no,'Asistente DBA').
aplica(medio,alto,sql,no,'Asistente DBA').
aplica(alto,alto,sql,no,'Asistente DBA').
aplica(medio,medio,sql,si,'Asistente DBA').
aplica(medio,alto,sql,si,'Asistente DBA').
aplica(alto,alto,sql,si,'Asistente DBA').
aplica(medio,medio,shell,si,'SysAdmin Jr').
aplica(medio,alto,shell,si,'SysAdmin Jr').
aplica(alto,alto,shell,si,'SysAdmin Jr').
aplica(bajo,bajo,shell,si,'SysAdmin Jr').
aplica(medio,bajo,shell,si,'SysAdmin Jr').
aplica(alto,bajo,shell,si,'SysAdmin Jr').


handle(Request) :-
   format(user_output,"I'm here~n",[]),
   cors_enable,
   http_read_json(Request, DictIn,[json_object(term)]),
   format(user_output,"Request is: ~p~n",[Request]),
   format(user_output,"DictIn is: ~p~n",[DictIn]),
   DictOut=DictIn,
   reply_json(DictOut).


:- server(8080).

from flask import Flask, render_template, request,redirect,url_for
"""
    /usuario/ (get)  - index/lista dos remedios cadastrados
    /usuario/ (post)
    /usuario/cadastro  (get) - renderizar o formulario para outro remedio
    /usuarios/<id> (get) obter dados do remedio
    /usuarios/<id>/edit(get) - renderizar o formulario para editar o remedio
    /usuarios/<id>/update(put) - atualizar o remedio
    /usuarios/<id>/delete (delete) - deleta o remedio
"""
app = Flask(__name__)
#rota para login do gogle

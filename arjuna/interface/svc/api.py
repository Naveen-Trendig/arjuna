import json
import mimetypes
import os
from urllib import response
import webbrowser
from arjuna import *
from functools import wraps

from flask import Flask, render_template, jsonify, request, Response
from flask_restful import Api, Resource
import webview
import app

gui_dir = os.path.join(os.path.dirname(__file__), '..',  'ui')  # development path
log_info(gui_dir)

gui_dir_abs = os.path.abspath(gui_dir)
log_info(os.path.abspath(gui_dir_abs))

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

ap = Flask(__name__)
# ap = Flask(__name__)
ap.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
api = Api(ap)


class HelloArjuna(Resource):

    # @api.representation("text/html")
    def get(self):
        return Response(render_template("index.html"), mimetype="text/html")

class Project(Resource):

    def post(self):
        dirs = r"D:\\vscode\\test_arjuna"
        # dirs = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        if dirs and len(dirs) > 0:
            directory = dirs
            if isinstance(directory, bytes):
                directory = directory.decode('utf-8')

            # listdir = app.make_tree(directory)

            # with open(r'D:\\vscode\\arjuna\\arjuna\\interface\\ui\\folder_structure.html', 'w', encoding="utf-8") as f:
            #     f.write(listdir)
            
        #     print(listdir)
        #     # log_info(listdir)
        #     response = {'status': 'ok', 'directory': listdir}
        # else:
        #     response = {'status': 'cancel'}

        # print(render_template("folder_structure.html", mimetypes="text/html", tree=app.make_tree(directory)))


        return Response(render_template("folder_structure.html", mimetypes="text/html", tree=app.make_tree(directory)))

class File(Resource):

    def get(self):
        
        import os
        path = r"D:\\vscode\\test_arjuna\\"
        content = ""
        file_path = request.args.get('file_path')
        print("request data: ", request)
        with open(os.path.join(path, file_path), 'r') as f:
             content = f.read()
          
        if content:
            response = {'status': 'ok', 'content': content}
        else:
            response = {'status': 'ok', 'content' : 'empty'} 
        # print(content)
        return jsonify(response)

    def post(self):
        # file_types = ("All files (*.*)")
        file = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        if file:
            response = {'status': 'ok', 'file': file}
        else:
            response = {'status': 'cancel'}
        return jsonify(response)

    def put(self):
        # file_types = ("All files (*.*)")
        # file = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        import os
        path = r"D:\\vscode\\test_arjuna\\"
        parent = request.get_json()['parent']
        file = request.get_json()['file']
        print("request data: ", request.get_json())
        # print("path", path)
        print("file", file)
        with open(os.path.join(path, parent, file), 'w') as fp:
            pass
        if file:
            response = {'status': 'ok', 'file': file}
        else:
            response = {'status': 'cancel'}
        return jsonify(response)

class SaveFile(Resource):

    def post(self):
        import os
        path = r"D:\\vscode\\test_arjuna\\"
        content = request.get_json()['content']
        file_path = request.get_json()['file_path'].strip()
        print(file_path)
        print(content)
        with open(os.path.join(path, file_path), 'w') as fp:
            fp.write(content)
        response = {'status': 'ok', 'save': 'sucess'}
        return jsonify(response)


class Folder(Resource):

    def put(self):
        import os
        path = r"D:\\vscode\\test_arjuna\\"
        folder =  request.get_json()['folder']
        parent =  request.get_json()['parent']
        print("request data: ", request.get_json())
        print("path", path)
        print("folder", folder)

        from pathlib import Path
        try:
            Path(os.path.join(path, parent, folder)).mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("folder already present.")
            response = {'status': 'ok', 'folder': 'folder already present.'}
        else:
            print("folder created.")
            response = {'status': 'ok', 'folder': folder}
        return jsonify(response)

    def delete(self):
        import os
        import shutil

        path = r"D:\\vscode\\test_arjuna\\"
        # folder_path = date = request.get_json()['path']
        folder_path = request.args.get('folder_path')
        print(os.path.join(path, folder_path))
        try:
            shutil.rmtree(os.path.join(path, folder_path))
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            print("folder is not deleted.")
            response = {'status': 'ok', 'folder': 'folder is not deleted.'}
        else:
            print("folder deleted.")
            response = {'status': 'ok', 'folder': 'folder deleted.'}
        return jsonify(response)


class Temp(Resource):

    def get(self):
        return Response(render_template("temp_folder_structure.html"), mimetype="text/html")

class DirTree(Resource):

    def get(self):
        dirs = r"D:\\vscode\\test_arjuna"
        return Response(render_template('dirtree.html', mimetype="text/html", tree=app.make_tree(dirs)))

api.add_resource(HelloArjuna, '/')
api.add_resource(Project, '/open/project')
api.add_resource(File, '/file')
api.add_resource(SaveFile, '/file/save')
api.add_resource(Folder, '/folder')
api.add_resource(Temp, '/do/stuff')
api.add_resource(DirTree, '/dir')

if __name__ == '__main__':
    ap.run(port=5001, use_evalex=False)




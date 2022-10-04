// isFolderCreated = false;

var xmlHttpRequst;

function getFolderContextMenu($node, tree){
	return {
        "Create": {
            "separator_before": false,
            "separator_after": true,
            "label": "Create",
            "action": false,
            "submenu": {
                "File": {
                    "seperator_before": false,
                    "seperator_after": false,
                    "label": "File",
                    action: function (obj) {
        
                        var path = tree.get_path($('#open-project-structure-root').jstree("get_selected", true)[0], '/');
                        createFile(path, 'New File');
                        $node = tree.create_node($node, { text: 'New File', icon: 'jstree-file', li_attr:{type:'file'} });
                        tree.deselect_all();
                        tree.select_node($node);
                    }
                },
                "Folder": {
                    "seperator_before": false,
                    "seperator_after": false,
                    "label": "Folder",
                    action: function (obj) {
                        // var id = obj.attr('id')
                        console.log("tree: ", tree);
                        // var path = obj.get_path('/');
                        var path = tree.get_path($('#open-project-structure-root').jstree("get_selected", true)[0], '/');
                        console.log(path);
                        createFolder(path, 'New Folder');
                        // tree.create_node($node, { text: 'New Folder', icon: 'jstree-folder', li_attr:{type:'folder'} });
                        // console.log("isCreated", isFolderCreated)
                        // if(isFolderCreated) {
                            // $node = tree.create_node($node, { text: 'New Folder', icon: 'jstree-folder', li_attr:{type:'folder'} });
                
                            // tree.deselect_all();
                            // tree.select_node($node);
                        // 	isFolderCreated=false;
                        // }
                    }
                }
            }
        },
        "Rename": {
            "separator_before": false,
            "separator_after": false,
            "label": "Rename",
            "action": function (obj) {
                tree.edit($node);
                renameFile("");                                    
            }
        },
        "Remove": {
            "separator_before": false,
            "separator_after": false,
            "label": "Remove",
            "action": function (obj) {
                if(confirm('confirm delete?')) {
                    var path = tree.get_path($('#open-project-structure-root').jstree("get_selected", true)[0], '/');
                    console.log(path);
                    deleteFolder(path)
                    tree.delete_node($node);
                }
            }
        }
	}
}
		
function getFileContextMenu($node, tree)
{
    return {
        "Rename": {
            "separator_before": false,
            "separator_after": false,
            "label": "Rename",
            "action": function (obj) {
                tree.edit($node);                                    
            }
        },
        "Remove": {
            "separator_before": false,
            "separator_after": false,
            "label": "Remove",
            "action": function (obj) {
                tree.delete_node($node);
            }
        }
    };
}

function openProjectHandler() {

    console.log(xmlHttpRequst.readyState)
    if (xmlHttpRequst.readyState == 4) {
        //  var response = JSON.parse(this.responseText);
        
        // totalHTML = "<ul>";
        // res = response["directory"];
        // for (var key in res) {
        //     outerHTML = "<li>" + JSON.stringify(key) + "<ul>";
        //     for (var i = 0; i < res[key].length; i++) {
        //         innerHTML = "<li>" + JSON.stringify(res[key][i]) + "</li>";
        //         outerHTML = outerHTML + innerHTML;
        //     }
        //     outerHTML = outerHTML + "</ul></li>";
        //     totalHTML = totalHTML + outerHTML;
        // }
        // totalHTML = totalHTML + "</ul>";

    document.getElementById("open-project-structure").innerHTML = this.responseText;
    $('#open-project-structure-root').jstree({
            "plugins" : [ "wholerow", "types", "contextmenu", "sort" ],
            "types" : {
                'file': {
                    'icon' : 'jstree-file'
                }
            },
            'core' : {
               "check_callback": true,
               "themes" : {
                    "variant" : "small",
                    'name': 'default-dark',
                    // 'responsive': true
                  }
            },
            'sort' : function(a, b) {
                a1 = this.get_node(a);
                b1 = this.get_node(b);
                if (a1.icon == b1.icon){
                    return (a1.text > b1.text) ? 1 : -1;
                } else {
                    return (a1.icon < b1.icon) ? 1 : -1;
                }
            },
            "contextmenu": {
                "items": function ($node) {
                    var tree = $("#open-project-structure-root").jstree(true);
                    if($node.li_attr.type === 'file')
                        return getFileContextMenu($node, tree);
                    else
                        return getFolderContextMenu($node, tree);                        
                    
                }
            }
        });

	// handle selecte events

	// $('#open-project-structure-root')
	// // listen for change event
	// .on('changed.jstree', function (e, data) {
	// 	var i, j, r = [];
	// 	var path = data.instance.get_path(data.node,'/');
	// 	for(i = 0, j = data.selected.length; i < j; i++) {
	// 		r.push(data.instance.get_node(data.selected[i]).text);
	// 	}
	// 	// $('#footer_content').html('Selected: ' + r.join(', '));
	// 	$('#footer_content').html('Selected: ' + path);
	// })
	// // create the instance
	// .jstree();

	$('#open-project-structure-root')
	// listen for select_node event
	.on('select_node.jstree', function (e, data) {
		// var file_name = data.instance.get_node(data.selected[0]).text;
		// console.log(data.node)
		// console.log(data.instance.get_node(data.selected[0]));
		// $('#fileContent').html('Folder/File Selected: ' + file_name);

		var node_id   = (data.node.id); // element id
        var type = $("#"+node_id).attr("type");
		console.log('selected type: ', type)
		if(type == 'file') {
			var file_path = data.instance.get_path(data.node,'/');
			console.log("file path: ", file_path)
			openFile(file_path);
		}
	})
	// create the instance
	.jstree();

    console.log('open project')

        // $('#open-project-structure-root').jstree();

        // $('#open-project-structure').jstree();
        // {
        //     "plugins" : [ "wholerow", "types" ],
        //     "types" : {
        //         // default: {
        //         //     'icon' : 'jstree-file'
        //         // },
        //         'file': {
        //             'icon' : 'jstree-file'
        //         }
        //     },
        //     'core' : {
        //        "themes" : {
        //             "variant" : "small"
        //           }
        //     //   'data' : {
        //     //     'url' : '/templates/folder_structure.html',
        //     //     'data' : function (node) {
        //     //       return { 'id' : node.id };
        //     //     }
        //     //   }
        //     }
        //   });

        // document.getElementsByTagName("body").innerHTML = "<script>$('#open-project-structure').jstree();</script>";
        // $('#open-project-structure').jstree();
        
        
    }
}

// $(function () { $('#open-project-structure').jstree(); });

function openFileHandler() {
    if (xmlHttpRequst.readyState == 4) {
        var response = JSON.parse(this.responseText);
        document.getElementById("fileContent").innerHTML = response['content'];
        // const reader = new FileReader();
        // ta = document.createElement("textarea");
        // ta.innerHTML = response["content"];
        // const currentDiv = document.getElementById("fileContent");
    }
}

function createFileHandler(response) {
    if (xmlHttpRequst.readyState == 4) {
        // var response = JSON.parse(this.responseText);
        alert('file saved succesfully.')
    }
}

function saveFileHandler(response) {
    if (xmlHttpRequst.readyState == 4) {
        alert('file saved succesfully.')
    }
}

function createFolderHandler(response) {
    if (xmlHttpRequst.readyState == 4) {
        var response = JSON.parse(this.responseText);
        // console.log('response: ', response)
        if(response.folder != 'folder already present.') {
            console.log('folder created succesfully..')
            alert('folder created succesfully.');
            // isFolderCreated = true;
            $node = $('#open-project-structure-root').jstree("get_selected", true)[0];
            console.log("current selected node: ", $node)
            $node = $('#open-project-structure-root').jstree().create_node($node, { text: 'New Folder', icon: 'jstree-folder', li_attr:{type:'folder'} });
            console.log("created node: ", $node)
                    
        }
        else {
            console.log('folder already present.')
            alert('folder already present.');
            // isFolderCreated = false;
        }
    }
}

function deleteFolderHandler() {
    if (xmlHttpRequst.readyState == 4) {
        var response = JSON.parse(this.responseText);
        // console.log('response: ', response)
        alert(response.folder);
    }

}

function doStuffHandler(response) {
    if (xmlHttpRequst.readyState == 4) {
        // var response = JSON.parse(this.responseText);
        // document.getElementById("stuff-container").innerHTML = this.responseText;
        // $("#folder-struct").jstree();
        
    }

}

function openProject() {
    doAjax("/open/project", "POST", openProjectHandler);
}

// function openFile() {
//     doAjax("/open/file",  "POST", openFileHandler);
// }

function openFile(file_path) {
    doAjax("/file?file_path=" + file_path,  "GET", openFileHandler);
}

function createFile(parent, file) {
    doAjax("/file",  "PUT", createFileHandler, {'parent':parent, 'file':file});
}

function saveFile() {
    file_path = $("#open-project-structure-root").jstree(true).get_path($('#open-project-structure-root').jstree("get_selected", true)[0], '\\')
    content = document.getElementById('fileContent').textContent;
    console.log('file path to save: ', file_path)
    doAjax("/file/save",  "POST", saveFileHandler, {'file_path':file_path, 'content':content});
}

function createFolder(parent, folder) {
    doAjax("/folder",  "PUT", createFolderHandler, {'parent':parent, 'folder':folder});
}

function deleteFolder(path) {
    doAjax("/folder?folder_path=" + path,  "DELETE", deleteFolderHandler);
}

function doStuff() {
    // doAjax("/do/stuff", "GET", doStuffHandler);
    $('#stuff-container').jstree({
        'core' : {
          'data' : {
            'url' : 'temp_folder_structure.html',
            'data' : function (node) {
              return { 'id' : node.id };
            }
          }
        }
      });
}

function toggleFullscreen() {
    doAjax("/fullscreen", "POST", doStuffHandler);
}

function openLink(e) {
    e.preventDefault()
    var request = {url: e.currentTarget.href}
    doAjax("/open-url", "POST", false, request)
}

// From https://gist.github.com/dharmavir/936328
function getHttpRequestObject()
{
    // Define and initialize as false

    // Mozilla/Safari/Non-IE
    if (window.XMLHttpRequest)
    {
        xmlHttpRequst = new XMLHttpRequest();
    }
    // IE
    else if (window.ActiveXObject)
    {
        xmlHttpRequst = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xmlHttpRequst;
}

// Does the AJAX call to URL specific with rest of the parameters
function doAjax(url, method, responseHandler, data)
{
    // Set the variables
    url = url || "";
    method = method || "GET";
    async = true;
    data = data || {};
    data.token = window.token;

    if(url == "") {
        alert("URL can not be null/blank");
        return false;
    }
    var xmlHttpRequest = getHttpRequestObject();

    // If AJAX supported
    if(xmlHttpRequest != false) {
        xmlHttpRequest.open(method, url, async);
        // Set request header (optional if GET method is used)
        if(method == "POST" ||  method == "PUT")  {
            xmlHttpRequest.setRequestHeader("Content-Type", "application/json");
        }
        // Assign (or define) response-handler/callback when ReadyState is changed.
        xmlHttpRequest.onreadystatechange = responseHandler;
        // Send data
        xmlHttpRequest.send(JSON.stringify(data));
    }
    else
    {
        alert("Please use browser with Ajax support.!");
    }
}
const { app, BrowserWindow } = require('electron')
let win

function createWindow () {
  //This is for editting.
  //var subpy = require('child_process').spawn('python',['src/server.py']);
  //This is for .exe file. 
  //var subpy = require('child_process').spawn('python',['resources/app/src/server.py']);

  console.log(__dirname);
  const win = new BrowserWindow({
    width: 400,
    height: 450,
    icon: __dirname+'/build/appx/icon.png',
    webPreferences: { 
      enableremotemodule: true,
      nodeIntegration: true
    } 
  })

  win.loadFile(__dirname+'/src/index.html')
  //win.webContents.openDevTools() //Showing a dev tool.
  win.setMenu(null);//Hiding a menu bar.
}

app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})
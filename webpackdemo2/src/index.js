import _ from "lodash";
import './style.css';
import Icon from './timg.jpg';
import printMe from './print.js';

function component() {
    var element = document.createElement('div');

    // Lodash（目前通过一个 script 脚本引入）对于执行这一行是必需的
    element.innerHTML = _.join(['Hello', 'webpack'], ' ');
    element.classList.add('hello');

    var btn = document.createElement('button');
    btn.innerHTML = 'Click me and check the console!';
    btn.onclick = printMe;

    element.appendChild(btn);

    var myicon = new Image();
    myicon.src = Icon;
    element.appendChild(myicon);

    return element;
}

document.body.appendChild(component());
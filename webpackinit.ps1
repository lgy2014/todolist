mkdir webpackdemo2
Set-Location webpackdemo2

cnpm init -y
cnpm install webpack webpack-cli --save-dev

cnpm install --save lodash

cnpm install --save-dev file-loader style-loader css-loader

# 加载数据
# cnpm install --save-dev csv-loader xml-loader

# 设定 HtmlWebpackPlugin
cnpm install --save-dev html-webpack-plugin
# 清理 /dist 文件夹
cnpm install clean-webpack-plugin --save-dev
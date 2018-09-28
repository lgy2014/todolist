const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  // entry: './src/index.js',
  entry:{
    app:'./src/index.ts',
    print:'./src/print.js'
  },
  devtool: 'inline-source-map',
  resolve:{
extensions:['.tsx','ts','js']
  },
  plugins:[
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title:'output management'
    })
  ],
  output: {
    // filename: 'bundle.js',
    filename:'[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  externals:{
    loadsh:{
      commonjs:'lodash',
      commonjs2:'lodash',
      amd:'lodash',
      root:'_'
    }
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use:'ts-loader',
        exclude:/node_modules/
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      },
      {
       test: /\.(png|svg|jpg|gif)$/,
       use:['file-loader']
      },
      {
       test: /\.(woff|woff2|eot|ttf|otf)$/,
       use:['file-loader']
      }
    ]
  }
};
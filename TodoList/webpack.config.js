const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');
module.exports = {
    mode: "development",
    entry:{
        index:"./index.js"
    },
    output: {
        filename: "static/js/[name].js"
    },
    resolve: {
        extensions: [".js",".vue"],
        modules: ['node_modules'],
        alias: {
            vue: 'vue/dist/vue.js',
        }
    },
    devServer: {
        inline:true,
        port:3000
    },
    module: {
        strictExportPresence: true,
        rules: [
            {
                test:/\.vue$/,
                loader: "vue-loader",
            },
            {
                test: /\.js$/,
                loader: "babel-loader",
                exclude:/node_modules/
            },
            {
                test:/\.css$/,
                loader: "style-loader!css-loader"
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template:"./index.html",
            inject:true,
            filename:"index.html",
        }),
        new VueLoaderPlugin(),
    ],
};
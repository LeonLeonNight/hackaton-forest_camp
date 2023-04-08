const path = require('path');
const { dirs } = require('../Settings/Constants');
const HtmlWebpackPlugin = require("../Plugins/HtmlWebpackPlugin");
const CleanWebpackPlugin = require("../Plugins/CleanWebpackPlugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    context: dirs.src,
	target: "web",
    entry: {
        main: path.join(dirs.src, "index.js"),
    },
    output: {
        path: dirs.dist,
        filename: '[name].bundle.js?hash=[hash]',
		publicPath: "/",
		assetModuleFilename: '[path][name][ext]'
    },
    plugins: [
        new MiniCssExtractPlugin({
			filename: "style.css?hash=[hash]",
		}),
        new CleanWebpackPlugin(),
        ...(new HtmlWebpackPlugin()),
    ],
    module: {
        rules: [
            // JavaScript
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            // изображения
            {
                test: /\.(?:ico|gif|png|jpg|jpeg)$/i,
                type: 'asset/resource',
            },
            // шрифты и SVG
            {
                test: /\.(woff(2)?|eot|ttf|otf|svg|)$/,
                type: 'asset/inline',
            },
            // CSS, PostCSS
            {
                test: /\.(css)$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
            },
        ],
    }
}
const {merge} = require('webpack-merge')
const BasicPart = require('./BasicPart')
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')

const buildWebpackConfig = merge(BasicPart, {
    mode: 'production',
    optimization: {
        minimizer: [
            new CssMinimizerPlugin(),
            new TerserPlugin()
        ]
    }
})

module.exports = new Promise((resolve, reject) => {
    resolve(buildWebpackConfig)
})
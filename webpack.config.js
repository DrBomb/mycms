module.exports = {
    entry:'./mycms/jsx/index.js',
    output:{
        path:'./mycms/static/bundles',
        filename:'index.js',
        publicPath:"/static/bundles/"    
    },
    devServer:{
        inline:true,
        port:3333
        //proxy: {
        //'/':{
        //    target:'http://localhost:5000'
        //    },
        //'/index':{
        //    target:'http://localhost:5000'
        //    }
        //}
    },
    module:{
        loaders:[
            {
                test:/\.js$/,
                exclude:/node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015','react']
                }
            }
        ]
    }
}

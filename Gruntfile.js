/**
 * Файл конфигурации сборки Grunt
 */
module.exports = function(grunt) {
    'use strict';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        browserify: {
            js: {
                options: {
                    browserifyOptions: {
                        // false в прод режиме
                        debug: false
                    }
                },
                // single entry point for our app
                src: 'tran/static/js/app/app.js',
                // compile to a single file to add in html
                dest: 'tran/static/js/build/app.js'
            }
        },

        less: {
            development: {
                files: {
                    'tran/static/css/less-styles.css': 'tran/static/less/main.less'
                }
            }
        },

        concat: {
            options: {
                sourceMap: true
            },
            css: {
                src: ['tran/static/css/less-styles.css'],
                dest: 'tran/static/css/styles.css'
            }
        },

        // перед выполнением конкатенации стилей, нужно удалить старый файл
        clean: {
            css: ["tran/static/css/styles.css"]
        },

        cssmin: {
            tran: {
                src: 'tran/static/css/styles.css',
                dest: 'tran/static/css/styles.min.css'
            }
        },

        uglify: {
            tran: {
                files: {
                    'tran/static/js/build/app.min.js': 'tran/static/js/build/app.js'
                }
            }
        },

        ngAnnotate: {
            options: {},
            tran: {
                files: {
                    'tran/static/js/build/app.js': 'tran/static/js/build/app.js'
                }
            }
        },

        watch: {
            less: {
                files: ["tran/static/less/**/*.less"],
                tasks: ['default']
            },
            js: {
                files: [
                    'tran/static/js/app/**/*.js'
                ],
                tasks: ['default']
            }
        }
    });

    // Load plugins here.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-ng-annotate');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-css');

    // Register tasks here.
    grunt.registerTask('default', [
        'clean', 'less', 'concat', 'cssmin',
        'browserify', 'ngAnnotate', 'uglify', 'watch'
    ]);
};
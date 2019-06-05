'use strict';

const path = require('path');

const _root = path.resolve(__dirname, '..');
const _prod_root = path.resolve(__dirname, '../../');

exports.root = function (args) {
    args = Array.prototype.slice.call(arguments, 0);

    return path.join.apply(path, [ _root ].concat(args));
};

exports.prod_root = function (args) {
    args = Array.prototype.slice.call(arguments, 0);

    return path.join.apply(path, [ _prod_root ].concat(args));
};

exports.assetsPath = function (_path) {
    return path.posix.join('static', _path);
};

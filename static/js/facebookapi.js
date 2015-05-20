/**
 * Created by bamsi on 20.05.2015.
 */
var Facebook = function () {
    'use strict';

    return {

        init: function (callback) {

            $.getScript('//connect.facebook.net/tr_TR/all.js', function () {
                FB.init({
                    appId  : '470627419759473',
                    status : true,
                    cookie : true
                });

                callback();
            });
        }
    };
}();
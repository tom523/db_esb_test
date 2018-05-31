// function errorAlert(message) {
//     var d = dialog({
//         width: 260,
//         title: '提示',
//         cancel: function (){},
//         ok: function() {},
//         okValue: '确定',
//         content: '<div class="king-notice-box king-notice-fail"><p class="king-notice-text">'+message+'</p></div>',
//         cancelValue: '取消',
//         cancel: function() {
//             // do something
//         }
//     });
//     d.show();
// }
//
// function successAlert(message) {
//     var d = dialog({
//         width: 260,
//         title: '提示',
//         cancel: function (){},
//         ok: function() {},
//         okValue: '确定',
//         content: '<div class="king-notice-box king-notice-success"><p class="king-notice-text">'+message+'</p></div>',
//         cancelValue: '取消',
//         cancel: function() {
//             // do something
//         }
//     });
//     d.show();
//
// }
//
// //待查询的门店ID必须是多个6位数字，且以英文逗号分隔的字符串
// function isArrayItemNo(str) {
//     for(var i=0; i<str.length; i++){
//         if(isNo(str[i])){
//             continue;
//         }else{
//             return false
//         }
//     }
//     return true;
// }
// function isNo(str) {
//     var reg=/^[0-9]{6}$/;
//     return reg.test(str);
// }


var myutils = {
    isNo: function (str) {
        var reg=/^[0-9]{6}$/;
        return reg.test(str);
    },

    isArrayItemNo: function (str) {
        for(var i=0; i<str.length; i++){
            if(myutils.isNo(str[i])){
                continue;
            }else{
                return false
            }
        }
        return true;
    },

    errorAlert: function (message) {
    var d = dialog({
        width: 260,
        title: '提示',
        cancel: function (){},
        ok: function() {},
        okValue: '确定',
        content: '<div class="king-notice-box king-notice-fail"><p class="king-notice-text">'+message+'</p></div>',
        cancelValue: '取消',
        cancel: function() {
            // do something
        }
    });
    d.show();
    },

    successAlert: function (title, message) {
        var d = dialog({
            width: 260,
            title: title,
            cancel: function (){},
            ok: function() {},
            okValue: '确定',
            content: '<div class="king-notice-box king-notice-success"><p class="king-notice-text">'+message+'</p></div>',
            cancelValue: '取消',
            cancel: function() {
                // do something
            }
        });
        d.show();
    },

    process_store_ids: function (store_ids) {
        var raw_store_id_array = $.trim(store_ids).split(/[,(\r\n)]/)
        var store_id_array = []
        for(var index in raw_store_id_array){
            if($.trim(raw_store_id_array[index]) != ""){
                store_id_array.push($.trim(raw_store_id_array[index]))
            }
        }
        if(store_id_array == ""){
            myutils.errorAlert("门店ID不能为空")
            return
        }else if(!myutils.isArrayItemNo(store_id_array)){
            myutils.errorAlert("非正常门店ID，门店ID必须是1个或多个6位数字，并且以英文逗号分隔。")
            return
        }
        return store_id_array
    }
    
}

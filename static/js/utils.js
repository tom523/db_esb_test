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
    isArrayItemNo: function (str) {
        for(var i=0; i<str.length; i++){
            if(isNo(str[i])){
                continue;
            }else{
                return false
            }
        }
        return true;
    },
    
    isNo: function (str) {
        var reg=/^[0-9]{6}$/;
        return reg.test(str);
    },
    
}

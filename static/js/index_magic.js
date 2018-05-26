$.get(site_url + 'get_menu_version', {}, function (res) {
    for (var key in res.data){
        $('#menu_version_select').append("<option value=" + key + ">" + res.data[key] + "</option>")
    }
})

function isNo(str) {
    var reg=/^[0-9]{6}$/;
    return reg.test(str);
}

function isArrayItemNo(str) {
    for(var i=0; i<str.length; i++){
        if(isNo(str[i])){
            continue;
        }else{
            return false
        }
    }
    return true;
}
function errorAlert(message) {
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
}

function successAlert(message) {
    var d = dialog({
        width: 260,
        title: '提示',
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

}

$('#new_menu_btn').click(function () {
    selectid = $('#menu_version_select option:selected').val()
    storecode = $('#store_code_id').val()
    if(storecode == ""){
        errorAlert("查询门店不能为空")
    }else if(!isArrayItemNo(storecode.split(','))){
        errorAlert("非正常门店ID，门店ID必须是1个或多个6位数字，并且以英文逗号分隔。")
    }else{
        $('#loding-img-2').show()
        $('#forbidden_layer').show()
        $.get(site_url + selectid + '/' + storecode.replace(/,/g,"_") + '/new_menu_m/', {}, function (res) {
            $('#loding-img-2').hide()
            $('#forbidden_layer').hide()
            if(res.code==0){
                successAlert("新上门店成功")
            }
        })
    }
})

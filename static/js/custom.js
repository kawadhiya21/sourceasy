function is_password_valid(){
	var password = document.getElementById("inputPassword3").value;
	//alert("password = " + password);
	var confirm_password = document.getElementById("inputPasswordConf3").value;
	//alert("confirm_password = " + confirm_password);
    	password_length = password.length;
    	if(password_length < 6)
        	{
	//	alert('testing');
		$("#signup_btn").prop("disabled",true);
        	$("#signup_btn").html("Your password needs "+(6-password_length)+" more character"+((password_length == 5) ? "" : "s")+".");
		}
	    else if (password != confirm_password)
		{
	    	$("#signup_btn").prop("disabled",true);
		$("#signup_btn").html("Your passwords do not match");
		}
    else if (password == confirm_password) 
		{
		    $("#signup_btn").prop("disabled",false);
		    $("#signup_btn").prop("class","btn btn-default btn-primary");
            $("#signup_btn").html("Let's go!");
		}
}
var secondary_image_index = 0;
var size_list = 2;
var detail_size = 0;
$('#add_more').click(function(){
    event.preventDefault();
    secondary_image_index++;
    temp_to_be_added = '<div class="form-group"><label for="inputSImage" class="col-sm-4 control-label">Image '+secondary_image_index+'</label><div class="col-sm-7"><input type="file" class="form-control" id="inputSImage" name="secondary_image_'+secondary_image_index+'"/></div></div>';
    $('#secondary_images').append(temp_to_be_added);
    $('#secondary_image_count').val(secondary_image_index);
});

$('#add_more_sizes').click(function(){
    event.preventDefault();
    size_list++;
    size_to_be_added = '<div class="form-group"><label for="inputProductName" class="col-sm-4 control-label">Size '+size_list+'</label><div class="col-sm-4"><input type="text" class="form-control" id="inputProductName" placeholder="Size of Product" name="name_'+size_list+'" /></div></div>';
    $('#size_list').append(size_to_be_added);
    $('#size_list_num').val(size_list);
});

$('#add_detail_size').click(function(){
    event.preventDefault();
    detail_size++;
    temp="";
    detail_add_template = '<tr id="'+detail_size+'"><td><div class="form-group"><div class="col-sm-10"><input style="width:120px;" class="form-control" type="text" name="pa'+detail_size+'" value=""></div></div></td>';
    product_size_num = $('#product_size_num').val();
    for(i=0;i<product_size_num;i++)
        {
        temp += '<td><input type="text" class="form-control" name="'+detail_size+'_'+size_array[i]+'" id="'+detail_size+'_'+size_array[i]+'" value=""></td>';
        }
    detail_add_template = detail_add_template+temp+'</tr>';
    $('#details_size').append(detail_add_template);
    $('#detail_size_num').val(detail_size); 
});

$('#f1, #f2, #f3, #f4, #lycra').keyup(function(){
    f1 = $('#f1').val();
    if(f1 == "") f1=0;
    f2 = $('#f2').val();
    if(f2 == "") f2=0;
    f3 = $('#f3').val();
    if(f3 == "") f3=0;
    f4 = $('#f4').val();
    if(f4 == "") f4=0;
    lycra = $('#lycra').val();
    if(lycra == "") lycra=0;
    total = parseInt(f1)+parseInt(f2)+parseInt(f3)+parseInt(f4)+parseInt(lycra);
    if(total == 100)
    {
        $('#submit_fabric_details').attr("disabled" , false);
        $('#total').html("Total :"+total);
        $('#submit_fabric_details').html("Let's Go");
    }
    else
    {
        $('#total').html("Total :"+total);
        $('#submit_fabric_details').html("Total percentage != 100");
        $('#submit_fabric_details').attr("disabled" , true);
    }
});

$('#base_knitted, #base_woven').change(function(){
    if(this.value == "knitted")
    {
        show = "baseknitted";
        hide = "basewoven"
    }
    else
    {
        show = "basewoven";
        hide = "baseknitted"
    }
    $('select[id='+show+']').css("display" , "block");
    $('select[id='+hide+']').css("display" , "none");
    $('select[id='+hide+']').val("");
});
var trim = 1;

$('#add_trim_button').click(function(){
event.preventDefault();
temp_to_be_added = '';
temp_to_be_added = '<div style="border:solid 2px;" id="trim'+trim+'">';
temp_to_be_added += 'Ignore this:<input type="checkbox" name="trim'+trim+'ignore" id="trim'+trim+'ignore" onchange="checkignore(this)"></br><h3><u>Trim '+trim+'</u></h3><div id="trim'+trim+'details">'; 
temp_fiber = '';
for(i=1;i<=4;i++){
    
    temp_fiber+='<div id="trim'+i+'fiber'+i+'"><h3>Fiber '+i+'</h3>Choose :<select name="trim'+trim+'fiber'+i+'_type"><option selected="true">Not Included</option>';
        for(j=0;j<fiber_array.length;j++){
            temp_fiber += '<option value="'+fiber_array[j]+'">'+fiber_array[j]+'</option>';
        }                            
    temp_fiber += '</select>Percentage(%):<input type="text" class="col-md-3" style="float:none!important" name="trim'+trim+'fiber'+i+'percentage" id="trim'+trim+'f1" value="0"></div>';
    
}
temp_to_be_added += temp_fiber;
temp_to_be_added += '<div id="trim'+trim+'lycra_div"><h3>Lycra</h3>Percentage(%):<input type="text" class="col-md-3" style="float:none!important" name="trim'+trim+'lycra" id="trim'+trim+'lycra" value="0"></div>';

temp_to_be_added += '<div class="form-group">GSM:<input type="text" name="trim'+trim+'gsm" id="trim'+trim+'gsm">Knitted:<input type="radio" value="knitted" name="trim'+trim+'construction_type" onchange="trimknitted(this)" id="trim'+trim+'knitted">Woven:<input type="radio" name="trim'+trim+'construction_type" onchange="trimwoven(this)" id="trim'+trim+'woven" value="woven">';

temp_to_be_added += '<select name="trim'+trim+'knitted" id="trim'+trim+'knitted" style="display:none;"><option selected="true">Not Included</option>';
temp_knitted = '';
for(i=0;i<knitted_array.length;i++){
    temp_knitted += '<option value="'+knitted_array[i]+'">'+knitted_array[i]+'</option>';
}
temp_to_be_added += temp_knitted;
temp_to_be_added += '</select>';

temp_to_be_added += '<select name="trim'+trim+'woven" id="trim'+trim+'woven" style="display:none;"><option selected="true">Not Included</option>';
temp_woven = '';
for(i=0;i<woven_array.length;i++){
    temp_woven += '<option value="'+woven_array[i]+'">'+woven_array[i]+'</option>';
}
temp_to_be_added += temp_woven;
temp_to_be_added += '</select></div>';
temp_to_be_added += '</div>';
$('#trim_fabric_count').val(trim);
trim++;
$('#trimfabric').append(temp_to_be_added);
});

function checkignore(ignore){
    id = ignore.id;
    num = id[4];
    value = $('#'+id).is(':checked');
    if(value) { $('#trim'+num+'details').css('display' , 'none'); }
    else { $('#trim'+num+'details').css('display' , 'block'); }
}

function trimknitted(knitted){
    id = knitted.id[4];
    $('select[id="trim'+id+'knitted"]').css('display','block');
    $('select[id="trim'+id+'woven"]').css('display','none');
}
function trimwoven(woven){
    id = woven.id[4];
    $('select[id="trim'+id+'woven"]').css('display','block');
    $('select[id="trim'+id+'knitted"]').css('display','none');
}    

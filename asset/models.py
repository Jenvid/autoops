from django.db import models


class asset(models.Model):
    hostname = models.CharField(max_length=64, verbose_name='主机名', null=True,blank=True,unique=True)
    network_ip = models.GenericIPAddressField(verbose_name='外网IP',null=True,blank=True)
    manage_ip = models.GenericIPAddressField(verbose_name='管理IP', null=True,blank=True)
    port = models.IntegerField(verbose_name='ssh端口', null=True,blank=True,default="22")
    model = models.CharField(max_length=128, verbose_name='型号', null=True,blank=True)
    system = models.CharField(max_length=128,verbose_name='系统版本',null=True,blank=True)
    system_user = models.ForeignKey(to="system_users",to_field='id', null=True,verbose_name='登陆用户',blank=True)
    data_center =  models.ForeignKey(to="data_centers",to_field='id', null=True,verbose_name='数据中心',blank=True)
    cabinet = models.CharField(max_length=64,verbose_name='机柜',null=True,blank=True)
    position = models.CharField(max_length=64,verbose_name='位置',null=True,blank=True)


    sn = models.CharField(max_length=64,verbose_name='序列号',null=True,blank=True)
    cpu = models.CharField(max_length=64,verbose_name='CPU',null=True,blank=True)
    memory = models.CharField(max_length=64, verbose_name='内存', null=True,blank=True)
    disk = models.CharField(max_length=256,verbose_name="硬盘",null=True,blank=True)
    uplink_port = models.CharField(max_length=256,verbose_name="上联端口",null=True,blank=True)

    ship_time = models.DateField(verbose_name="出厂时间",default="1970-01-01")
    end_time = models.DateField(verbose_name="到保时间",default="1970-01-01")

    product_line =  models.ManyToManyField(to="product_lines",verbose_name='产品线',blank=True)
    is_active = models.BooleanField(default=True, verbose_name=('是否启用'))
    ps = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)

    ctime= models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间',blank=True)
    utime = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间',blank=True)


    class  Meta:
        db_table ="asset"
        verbose_name="资产管理"
        verbose_name_plural = '资产管理'


    def __str__(self):
        return self.network_ip

class   product_lines(models.Model):
    product_line_list = models.CharField(max_length=128, verbose_name='产品线',null=True,blank=True)


    class Meta:
        db_table = "product_lines"
        verbose_name = "产品线"
        verbose_name_plural = '产品线'

    def __str__(self):
        return self.product_line_list

class   data_centers(models.Model):
    data_center_list = models.CharField(max_length=128, verbose_name='数据中心', null=True)

    class Meta:
        db_table = "data_centers"
        verbose_name = "数据中心"
        verbose_name_plural = '数据中心'

    def __str__(self):
        return self.data_center_list


class  system_users(models.Model):
    name = models.CharField(max_length=128, unique=True,null=True,verbose_name=('名称'))
    username = models.CharField(max_length=64,null=True,blank=True, verbose_name=('登陆用户'))
    password = models.CharField(max_length=256, blank=True,null=True,verbose_name=('登陆密码'))
    ps = models.CharField(max_length=1024,verbose_name="备注",null=True,blank=True)
    ctime= models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间',blank=True)
    utime = models.DateTimeField(auto_now=True, null=True,verbose_name='更新时间',blank=True)

    def __str__(self):
        return self.name

    class  Meta:
        db_table ="system_users"
        verbose_name="系统登陆用户"
        verbose_name_plural = '系统登陆用户'


class performance(models.Model):

    cpu_use = models.CharField(verbose_name='CPU使用率', null=True,blank=True,max_length=32)
    mem_use = models.CharField(verbose_name='内存使用率', max_length=32, null=True,blank=True)
    in_use = models.CharField(verbose_name='进流量', max_length=32, null=True,blank=True)
    out_use = models.CharField(verbose_name='出流量', max_length=32, null=True,blank=True)
    server = models.ForeignKey('asset',on_delete=callable, null=True,blank=True,)

    cdate = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    udate = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table = 'performance'
        verbose_name = '监控状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpu_use
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

UserAdmin=get_user_model()



class Cpu(models.Model):

    # Unique identifier for each CPU entry, automatically incremented.
    id = models.AutoField(primary_key=True, unique=True)
        
    brand_choices = (
        ('INTEL', 'Intel'),
        ('AMD', 'AMD'),
        ('IBM', 'IBM'),
        ('APPLE', 'Apple'),
        ('QUALCOMM', 'Qualcomm'),
        ('ARM', 'ARM'),
        ('NVIDIA', 'Nvidia'),
        ('MEDIATEK', 'MediaTek'),
        ('TEXAS_INSTRUMENTS', 'Texas Instruments'),
    )
    # The brand or manufacturer of the CPU (e.g., Intel, AMD).
    cpu_brand = models.CharField(max_length=220, choices=brand_choices, default='INTEL')
    # Example: "Intel" for Intel Core i5-13420H, "AMD" for AMD Ryzen 7 5800X.

    # The series or family to which the CPU belongs (e.g., Core, Ryzen).
    cpu_series = models.CharField(max_length=220)
    # Example: "Core" for Intel Core i5-13420H, "Ryzen" for AMD Ryzen 7 5800X.

    # The specific model name or number of the CPU.
    cpu_model = models.CharField(max_length=220)
    # Example: "i5-13420H" for Intel, "Ryzen 7 5800X" for AMD.

    # The generation of the CPU, indicating improvements in architecture.
    cpu_generation = models.IntegerField()
    # Example: 13 for Intel Core i5-13420H (13th Gen), 5 for AMD Ryzen 7 5800X (5th Gen).

    # SKU (Stock Keeping Unit) number, unique identifier within a generation.
    cpu_sku = models.CharField(max_length=50)
    # Example: "13420H" for Intel Core i5, "5800X" for AMD Ryzen 7.

    # The total number of cores in the CPU.
    total_cores = models.IntegerField()
    # Example: 6 for Intel Core i5-13420H, 8 for AMD Ryzen 7 5800X.

    # Number of high-performance cores (for hybrid architecture CPUs).
    performance_cores = models.IntegerField(null=True, blank=True)
    # Example: 4 for Intel Core i5-13420H. Leave null for AMD Ryzen 7 5800X.

    # Number of efficiency cores (for hybrid architecture CPUs).
    efficiency_cores = models.IntegerField(null=True, blank=True)
    # Example: 2 for Intel Core i5-13420H. Leave null for AMD Ryzen 7 5800X.

    # The number of threads the CPU can handle simultaneously.
    threads = models.IntegerField()
    # Example: 12 for Intel Core i5-13420H, 16 for AMD Ryzen 7 5800X.

    # The base clock speed of the CPU, in GHz.
    base_clock_speed = models.DecimalField(max_digits=5, decimal_places=2)
    # Example: 3.00 GHz for Intel Core i5-13420H, 3.80 GHz for AMD Ryzen 7 5800X.

    # The maximum boost clock speed of the CPU, in GHz.
    boost_clock_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # Example: 4.60 GHz for Intel Core i5-13420H, 4.70 GHz for AMD Ryzen 7 5800X.

    # The size of the Level 1 cache memory, in MB.
    l1_cache = models.DecimalField(max_digits=5, decimal_places=2)
    # Example: 0.48 MB for Intel Core i5-13420H, 0.512 MB for AMD Ryzen 7 5800X.

    # The size of the Level 2 cache memory, in MB.
    l2_cache = models.DecimalField(max_digits=5, decimal_places=2)
    # Example: 2 MB for Intel Core i5-13420H, 4 MB for AMD Ryzen 7 5800X.

    # The size of the Level 3 cache memory, in MB.
    l3_cache = models.DecimalField(max_digits=5, decimal_places=2)
    # Example: 8 MB for Intel Core i5-13420H, 32 MB for AMD Ryzen 7 5800X.

    # Thermal Design Power (TDP), indicating the maximum amount of heat the CPU is expected to generate, in watts.
    tdp = models.IntegerField()
    # Example: 45 watts for Intel Core i5-13420H, 105 watts for AMD Ryzen 7 5800X.

    # The maximum operating temperature the CPU can safely reach, in °C.
    max_operating_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    # Example: 100.00 °C for Intel Core i5-13420H, 95.00 °C for AMD Ryzen 7 5800X.

    # Indicates whether the CPU has integrated graphics.
    has_integrated_graphics = models.BooleanField(default=False)
    # Example: True for Intel Core i5-13420H, False for AMD Ryzen 7 5800X.

    # The model name of the integrated GPU, if present.
    integrated_graphics_model = models.CharField(max_length=220, null=True, blank=True)
    # Example: "Intel UHD Graphics" for Intel Core i5-13420H. Leave null for AMD Ryzen 7 5800X.

    # The maximum frequency of the integrated GPU, in GHz.
    integrated_graphics_max_frequency = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # Example: 1.45 GHz for Intel Core i5-13420H. Leave null for AMD Ryzen 7 5800X.

    # The manufacturing process size used for the CPU, in nanometers (nm).
    lithography = models.IntegerField()
    # Example: 10 nm for Intel Core i5-13420H, 7 nm for AMD Ryzen 7 5800X.

    # The official release date of the CPU.
    release_date = models.DateField()
    # Example: "2023-02-01" for Intel Core i5-13420H, "2020-11-05" for AMD Ryzen 7 5800X.

    # Indicates whether the CPU supports Hyper-Threading (Intel) or SMT (AMD).
    supports_hyperthreading = models.BooleanField(default=False)
    # Example: True for both Intel Core i5-13420H and AMD Ryzen 7 5800X.

    # Indicates whether the CPU supports virtualization technologies like Intel VT-x or AMD-V.
    supports_virtualization = models.BooleanField(default=True)
    # Example: True for both Intel Core i5-13420H and AMD Ryzen 7 5800X.

    # Indicates whether the CPU can be overclocked for higher performance.
    supports_overclocking = models.BooleanField(default=False)
    # Example: False for Intel Core i5-13420H, True for AMD Ryzen 7 5800X.

    def __str__(self) -> str:
        return f"{self.cpu_brand} - {self.cpu_series} - {self.cpu_model}"



class Ram(models.Model):
    # Unique identifier for each RAM entry, automatically incremented.
    id = models.AutoField(primary_key=True, unique=True)
    
    # The brand or manufacturer of the RAM (e.g., Corsair, G.Skill).
    ram_brand = models.CharField(max_length=220)
    # Example: "Corsair", "G.Skill".
    
    # The type of RAM (e.g., DDR4, DDR5).
    ram_type = models.CharField(max_length=50)
    # Example: "DDR4", "DDR5".

    # The size of the RAM module, in GB.
    ram_size = models.IntegerField()
    # Example: 16 for 16 GB, 32 for 32 GB.

    # The speed or frequency of the RAM, in MHz.
    ram_speed = models.IntegerField()
    # Example: 3200 MHz, 3600 MHz.

    # The CAS latency of the RAM, indicating the delay between a command and the time the data is available.
    cas_latency = models.IntegerField()
    # Example: 16 for CAS latency of 16.

    # The voltage required by the RAM module to operate, in volts.
    voltage = models.DecimalField(max_digits=4, decimal_places=2)
    # Example: 1.35 volts, 1.2 volts.

    # The form factor of the RAM (e.g., DIMM, SO-DIMM).
    form_factor = models.CharField(max_length=50)
    # Example: "DIMM" for desktops, "SO-DIMM" for laptops.

    # The official release date of the RAM.
    release_date = models.DateField()
    # Example: "2022-01-01" for a RAM module released in January 2022.

    def __str__(self):
        return f"{self.ram_brand} - {self.ram_type} - {self.ram_size}"


class Gpu(models.Model):
    # Unique identifier for each GPU entry, automatically incremented.
    id = models.AutoField(primary_key=True, unique=True)
    
    # The brand or manufacturer of the GPU (e.g., Nvidia, AMD).
    gpu_brand = models.CharField(max_length=220)
    # Example: "Nvidia", "AMD".

    # The series or family to which the GPU belongs (e.g., RTX, Radeon).
    gpu_series = models.CharField(max_length=220)
    # Example: "RTX" for Nvidia, "Radeon" for AMD.

    # The specific model name or number of the GPU.
    gpu_model = models.CharField(max_length=220)
    # Example: "RTX 3050", "Radeon RX 6800".

    # The size of the GPU memory, in GB.
    memory_size = models.IntegerField()
    # Example: 8 for 8 GB, 12 for 12 GB.

    # The type of memory used in the GPU (e.g., GDDR6, HBM2).
    memory_type = models.CharField(max_length=50)
    # Example: "GDDR6", "HBM2".

    # The memory clock speed of the GPU, in MHz.
    memory_clock_speed = models.IntegerField()
    # Example: 1750 MHz for some GPUs.

    # The core clock speed of the GPU, in MHz.
    core_clock_speed = models.IntegerField()
    # Example: 1500 MHz, 1605 MHz.

    # The boost clock speed of the GPU, in MHz.
    boost_clock_speed = models.IntegerField(null=True, blank=True)
    # Example: 1777 MHz, 1845 MHz.

    # The number of CUDA cores (Nvidia) or Stream Processors (AMD) in the GPU.
    cuda_cores = models.IntegerField(null=True, blank=True)
    stream_processors = models.IntegerField(null=True, blank=True)
    # Example: 2560 CUDA cores for Nvidia RTX 3050, 3840 Stream Processors for AMD RX 6800.

    # The TDP (Thermal Design Power) of the GPU, in watts.
    tdp = models.IntegerField()
    # Example: 130 watts for Nvidia RTX 3050, 250 watts for AMD RX 6800.

    # The interface used to connect the GPU to the motherboard (e.g., PCIe 4.0).
    interface = models.CharField(max_length=50)
    # Example: "PCIe 4.0".

    # The official release date of the GPU.
    release_date = models.DateField()
    # Example: "2021-07-01" for a GPU released in July 2021.


    def __str__(self):
        return f"{self.gpu_brand} - {self.gpu_model} - {self.memory_size}"






class Brand(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    brand_name=models.CharField(max_length=220)
    country=models.CharField(max_length=220)
    # oldness=
    series=models.CharField(max_length=220,null=True,blank=True)

    def __str__(self):
        return f"{self.brand_name}"




class LaptopProduct(models.Model): 
    id = models.AutoField(primary_key=True,unique=True) 
    # brand = models.CharField(max_length=220 , ) 
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    model = models.CharField(max_length=220 ) 
    series =  models.CharField(max_length=220 )
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE,related_name='ram_laptops')
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE,related_name='gpu_laptops') 
    
    # cpu = models.CharField(max_length=220 )
    # gpu = models.CharField(max_length=220,default='null' )

    create_time=models.DateTimeField(auto_now_add=True)
    update_time =models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=100,decimal_places=0)
    images=models.ImageField(blank=True,null=True) 
    general='general'
    ai_programing='Ai'
    backend_devops_programing='backend_devops'
    graphic='graphic'
    Architecture='architecture'
    enginering='enginiering'
    iot='iot' 
    usage_choices=(
        (general,'عمومی'),
        (ai_programing,'هوش  مصنوعی'),
        (backend_devops_programing,'برنامه نویس  بکند و فرانت و دواپس'),
        (graphic,'گرافیک'),
        (Architecture,'معماری'),
        (enginering,'مهندسی'),
        (iot,'iot'),
        )
    
    usage= models.CharField(
        max_length=220,
        choices=usage_choices,
        default=general ,)
    # battery= 
    description=models.TextField(blank=True)
    user_maker=models.ForeignKey(UserAdmin,default=1,
                                 on_delete=models.CASCADE,
                                 related_name='user_admin_laptops',
                                 )
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True) 
    battery = models.CharField(max_length=100, blank=True)
   
    # made_in=
    def __str__(self) -> str:
        return (f"{self.brand} - {self.series} - {self.model}")


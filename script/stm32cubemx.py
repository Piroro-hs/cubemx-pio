from SCons.Script import DefaultEnvironment

flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

env = DefaultEnvironment()

opt = '-O2'

cpu = '-mcpu=%s' % env.BoardConfig().get('build.cpu')
fpu = '-mfpu=fpv4-sp-d16'
float_abi = '-mfloat-abi=hard'
mcu = [cpu, '-mthumb', fpu, float_abi]

env.Append(
    CPPDEFINES=[
        'USE_HAL_DRIVER',
        env.BoardConfig().get('build.variant', '').upper()
    ],

    ASFLAGS=flatten([
        '-x',
        'assembler-with-cpp',
        mcu,
        opt,
        '-Wall',
        '-fdata-sections',
        '-ffunction-sections'
    ]),

    CPPFLAGS=flatten([
        mcu,
        '--specs=nano.specs',
        opt,
        '-Wall',
        '-fdata-sections',
        '-ffunction-sections'
    ]),

    CXXFLAGS=[
        '-std=c++17',
        '-fno-rtti',
        '-fno-exceptions'
    ],

    LINKFLAGS=flatten([
        mcu,
        '--specs=nano.specs',
        '--specs=nosys.specs',
        '-Tlib/CubeMX/STM32F446RETx_FLASH.ld',
        '-Wl,--gc-sections',
    ])
)

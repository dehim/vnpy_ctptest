import platform

from setuptools import Extension, setup


def get_ext_modules() -> list:
    """
    获取三方模块

    Linux需要编译封装接口
    Windows直接使用预编译的pyd即可
    Mac由于缺乏二进制库支持无法使用
    """
    if platform.system() != "Linux":
        return []

    compiler_flags = [
        "-std=c++17",
        "-O3",
        "-Wno-delete-incomplete", "-Wno-sign-compare",
    ]
    extra_link_args = ["-lstdc++"]
    runtime_library_dirs = ["$ORIGIN"]

    vnctpmd = Extension(
        "vnpy_ctptest.api.vnctpmd",
        [
            "vnpy_ctptest/api/vnctp/vnctpmd/vnctpmd.cpp",
        ],
        include_dirs=["vnpy_ctptest/api/include",
                      "vnpy_ctptest/api/vnctp"],
        define_macros=[],
        undef_macros=[],
        library_dirs=["vnpy_ctptest/api/libs", "vnpy_ctptest/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=compiler_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        depends=[],
        language="cpp",
    )

    vnctptd = Extension(
        "vnpy_ctptest.api.vnctptd",
        [
            "vnpy_ctptest/api/vnctp/vnctptd/vnctptd.cpp",
        ],
        include_dirs=["vnpy_ctptest/api/include",
                      "vnpy_ctptest/api/vnctp"],
        define_macros=[],
        undef_macros=[],
        library_dirs=["vnpy_ctptest/api/libs", "vnpy_ctptest/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=compiler_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        depends=[],
        language="cpp",
    )

    return [vnctptd, vnctpmd]


setup(
    ext_modules=get_ext_modules(),
)

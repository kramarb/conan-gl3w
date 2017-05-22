project(gl3w)
cmake_minimum_required(VERSION 2.8.12)

set(SRC_FILES
	gl3w/src/gl3w.c
	)

include_directories(
	gl3w/include
	)

add_library(gl3w STATIC ${SRC_FILES})


# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Github/portfolio/teachingassistent/aflevering1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/aflevering1.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/aflevering1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/aflevering1.dir/flags.make

CMakeFiles/aflevering1.dir/main.c.o: CMakeFiles/aflevering1.dir/flags.make
CMakeFiles/aflevering1.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/aflevering1.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/aflevering1.dir/main.c.o   -c /mnt/c/Github/portfolio/teachingassistent/aflevering1/main.c

CMakeFiles/aflevering1.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/aflevering1.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /mnt/c/Github/portfolio/teachingassistent/aflevering1/main.c > CMakeFiles/aflevering1.dir/main.c.i

CMakeFiles/aflevering1.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/aflevering1.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /mnt/c/Github/portfolio/teachingassistent/aflevering1/main.c -o CMakeFiles/aflevering1.dir/main.c.s

# Object files for target aflevering1
aflevering1_OBJECTS = \
"CMakeFiles/aflevering1.dir/main.c.o"

# External object files for target aflevering1
aflevering1_EXTERNAL_OBJECTS =

aflevering1: CMakeFiles/aflevering1.dir/main.c.o
aflevering1: CMakeFiles/aflevering1.dir/build.make
aflevering1: CMakeFiles/aflevering1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable aflevering1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/aflevering1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/aflevering1.dir/build: aflevering1

.PHONY : CMakeFiles/aflevering1.dir/build

CMakeFiles/aflevering1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/aflevering1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/aflevering1.dir/clean

CMakeFiles/aflevering1.dir/depend:
	cd /mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Github/portfolio/teachingassistent/aflevering1 /mnt/c/Github/portfolio/teachingassistent/aflevering1 /mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug /mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug /mnt/c/Github/portfolio/teachingassistent/aflevering1/cmake-build-debug/CMakeFiles/aflevering1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/aflevering1.dir/depend


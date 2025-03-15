cmake_minimum_required(VERSION 3.8)
project(simple_box_ws)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Bağımlılıkları bul
find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Dosyaları doğru şekilde yükle
install(DIRECTORY launch/ DESTINATION share/${CMAKE_PROJECT_NAME}/launch)
install(DIRECTORY worlds/ DESTINATION share/${CMAKE_PROJECT_NAME}/worlds)
install(DIRECTORY models/ DESTINATION share/${CMAKE_PROJECT_NAME}/models)

# Launch dosyalarını yükle
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
  FILES_MATCHING PATTERN "*.py"
)

ament_package()

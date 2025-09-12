################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/FatFS/diskio.c \
../Core/Src/FatFS/ff.c 

OBJS += \
./Core/Src/FatFS/diskio.o \
./Core/Src/FatFS/ff.o 

C_DEPS += \
./Core/Src/FatFS/diskio.d \
./Core/Src/FatFS/ff.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/FatFS/%.o Core/Src/FatFS/%.su Core/Src/FatFS/%.cyclo: ../Core/Src/FatFS/%.c Core/Src/FatFS/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L475xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src-2f-FatFS

clean-Core-2f-Src-2f-FatFS:
	-$(RM) ./Core/Src/FatFS/diskio.cyclo ./Core/Src/FatFS/diskio.d ./Core/Src/FatFS/diskio.o ./Core/Src/FatFS/diskio.su ./Core/Src/FatFS/ff.cyclo ./Core/Src/FatFS/ff.d ./Core/Src/FatFS/ff.o ./Core/Src/FatFS/ff.su

.PHONY: clean-Core-2f-Src-2f-FatFS


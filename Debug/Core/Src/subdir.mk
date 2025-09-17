################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/DS18B20.c \
../Core/Src/INA3221.c \
../Core/Src/RTC.c \
../Core/Src/SIM7000.c \
../Core/Src/battery_charger.c \
../Core/Src/callbacks.c \
../Core/Src/extflash_hal.c \
../Core/Src/init.c \
../Core/Src/leds.c \
../Core/Src/lsm6dsv16x_reg.c \
../Core/Src/lsm6dsv16x_rw.c \
../Core/Src/main.c \
../Core/Src/process.c \
../Core/Src/psram.c \
../Core/Src/stm32l4xx_hal_msp.c \
../Core/Src/stm32l4xx_it.c \
../Core/Src/syscalls.c \
../Core/Src/sysmem.c \
../Core/Src/system_stm32l4xx.c 

OBJS += \
./Core/Src/DS18B20.o \
./Core/Src/INA3221.o \
./Core/Src/RTC.o \
./Core/Src/SIM7000.o \
./Core/Src/battery_charger.o \
./Core/Src/callbacks.o \
./Core/Src/extflash_hal.o \
./Core/Src/init.o \
./Core/Src/leds.o \
./Core/Src/lsm6dsv16x_reg.o \
./Core/Src/lsm6dsv16x_rw.o \
./Core/Src/main.o \
./Core/Src/process.o \
./Core/Src/psram.o \
./Core/Src/stm32l4xx_hal_msp.o \
./Core/Src/stm32l4xx_it.o \
./Core/Src/syscalls.o \
./Core/Src/sysmem.o \
./Core/Src/system_stm32l4xx.o 

C_DEPS += \
./Core/Src/DS18B20.d \
./Core/Src/INA3221.d \
./Core/Src/RTC.d \
./Core/Src/SIM7000.d \
./Core/Src/battery_charger.d \
./Core/Src/callbacks.d \
./Core/Src/extflash_hal.d \
./Core/Src/init.d \
./Core/Src/leds.d \
./Core/Src/lsm6dsv16x_reg.d \
./Core/Src/lsm6dsv16x_rw.d \
./Core/Src/main.d \
./Core/Src/process.d \
./Core/Src/psram.d \
./Core/Src/stm32l4xx_hal_msp.d \
./Core/Src/stm32l4xx_it.d \
./Core/Src/syscalls.d \
./Core/Src/sysmem.d \
./Core/Src/system_stm32l4xx.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/%.o Core/Src/%.su Core/Src/%.cyclo: ../Core/Src/%.c Core/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L475xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src

clean-Core-2f-Src:
	-$(RM) ./Core/Src/DS18B20.cyclo ./Core/Src/DS18B20.d ./Core/Src/DS18B20.o ./Core/Src/DS18B20.su ./Core/Src/INA3221.cyclo ./Core/Src/INA3221.d ./Core/Src/INA3221.o ./Core/Src/INA3221.su ./Core/Src/RTC.cyclo ./Core/Src/RTC.d ./Core/Src/RTC.o ./Core/Src/RTC.su ./Core/Src/SIM7000.cyclo ./Core/Src/SIM7000.d ./Core/Src/SIM7000.o ./Core/Src/SIM7000.su ./Core/Src/battery_charger.cyclo ./Core/Src/battery_charger.d ./Core/Src/battery_charger.o ./Core/Src/battery_charger.su ./Core/Src/callbacks.cyclo ./Core/Src/callbacks.d ./Core/Src/callbacks.o ./Core/Src/callbacks.su ./Core/Src/extflash_hal.cyclo ./Core/Src/extflash_hal.d ./Core/Src/extflash_hal.o ./Core/Src/extflash_hal.su ./Core/Src/init.cyclo ./Core/Src/init.d ./Core/Src/init.o ./Core/Src/init.su ./Core/Src/leds.cyclo ./Core/Src/leds.d ./Core/Src/leds.o ./Core/Src/leds.su ./Core/Src/lsm6dsv16x_reg.cyclo ./Core/Src/lsm6dsv16x_reg.d ./Core/Src/lsm6dsv16x_reg.o ./Core/Src/lsm6dsv16x_reg.su ./Core/Src/lsm6dsv16x_rw.cyclo ./Core/Src/lsm6dsv16x_rw.d ./Core/Src/lsm6dsv16x_rw.o ./Core/Src/lsm6dsv16x_rw.su ./Core/Src/main.cyclo ./Core/Src/main.d ./Core/Src/main.o ./Core/Src/main.su ./Core/Src/process.cyclo ./Core/Src/process.d ./Core/Src/process.o ./Core/Src/process.su ./Core/Src/psram.cyclo ./Core/Src/psram.d ./Core/Src/psram.o ./Core/Src/psram.su ./Core/Src/stm32l4xx_hal_msp.cyclo ./Core/Src/stm32l4xx_hal_msp.d ./Core/Src/stm32l4xx_hal_msp.o ./Core/Src/stm32l4xx_hal_msp.su ./Core/Src/stm32l4xx_it.cyclo ./Core/Src/stm32l4xx_it.d ./Core/Src/stm32l4xx_it.o ./Core/Src/stm32l4xx_it.su ./Core/Src/syscalls.cyclo ./Core/Src/syscalls.d ./Core/Src/syscalls.o ./Core/Src/syscalls.su ./Core/Src/sysmem.cyclo ./Core/Src/sysmem.d ./Core/Src/sysmem.o ./Core/Src/sysmem.su ./Core/Src/system_stm32l4xx.cyclo ./Core/Src/system_stm32l4xx.d ./Core/Src/system_stm32l4xx.o ./Core/Src/system_stm32l4xx.su

.PHONY: clean-Core-2f-Src


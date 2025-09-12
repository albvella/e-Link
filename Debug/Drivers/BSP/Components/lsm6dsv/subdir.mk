################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (12.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/Components/lsm6dsv/lsm6dsv.c \
../Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.c 

OBJS += \
./Drivers/BSP/Components/lsm6dsv/lsm6dsv.o \
./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.o 

C_DEPS += \
./Drivers/BSP/Components/lsm6dsv/lsm6dsv.d \
./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/Components/lsm6dsv/%.o Drivers/BSP/Components/lsm6dsv/%.su Drivers/BSP/Components/lsm6dsv/%.cyclo: ../Drivers/BSP/Components/lsm6dsv/%.c Drivers/BSP/Components/lsm6dsv/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L475xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -I../Drivers/BSP/Components/lsm6dsv -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-Components-2f-lsm6dsv

clean-Drivers-2f-BSP-2f-Components-2f-lsm6dsv:
	-$(RM) ./Drivers/BSP/Components/lsm6dsv/lsm6dsv.cyclo ./Drivers/BSP/Components/lsm6dsv/lsm6dsv.d ./Drivers/BSP/Components/lsm6dsv/lsm6dsv.o ./Drivers/BSP/Components/lsm6dsv/lsm6dsv.su ./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.cyclo ./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.d ./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.o ./Drivers/BSP/Components/lsm6dsv/lsm6dsv_reg.su

.PHONY: clean-Drivers-2f-BSP-2f-Components-2f-lsm6dsv


#include "user_main.h"

#include "stm32f4xx_hal.h"

auto setup() -> void {}

auto loop() -> void {
  HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
  HAL_Delay(500);
}

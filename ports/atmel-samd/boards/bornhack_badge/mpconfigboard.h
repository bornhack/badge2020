#define MICROPY_HW_BOARD_NAME "Bornhack Badge"
#define MICROPY_HW_MCU_NAME "samd21g18"

#define MICROPY_HW_LED_STATUS   (&pin_PB08)

#define SPI_FLASH_MOSI_PIN          &pin_PA22
#define SPI_FLASH_MISO_PIN          &pin_PA21
#define SPI_FLASH_SCK_PIN           &pin_PA23
#define SPI_FLASH_CS_PIN            &pin_PA20

// These are pins not to reset.
#define MICROPY_PORT_A        (PORT_PA00 | PORT_PA01)
#define MICROPY_PORT_B        (0)
#define MICROPY_PORT_C        (0)

#define DEFAULT_I2C_BUS_SCL (&pin_PA09)
#define DEFAULT_I2C_BUS_SDA (&pin_PA08)

#define DEFAULT_SPI_BUS_SCK (&pin_PA23)
#define DEFAULT_SPI_BUS_MOSI (&pin_PA22)
#define DEFAULT_SPI_BUS_MISO (&pin_PA21)

#define DEFAULT_UART_BUS_RX (&pin_PA05)
#define DEFAULT_UART_BUS_TX (&pin_PA04)

// USB is always used internally so skip the pin objects for it.
#define IGNORE_PIN_PA24     1
#define IGNORE_PIN_PA25     1

// Not connected
// #define IGNORE_PIN_PA00     1
// #define IGNORE_PIN_PA01     1
// #define IGNORE_PIN_PA02     1
// #define IGNORE_PIN_PA03     1
// #define IGNORE_PIN_PB09     1
// #define IGNORE_PIN_PA06     1
// #define IGNORE_PIN_PA07     1
// #define IGNORE_PIN_PA16     1
// #define IGNORE_PIN_PA17     1
// #define IGNORE_PIN_PA18     1
// #define IGNORE_PIN_PA19     1
// #define IGNORE_PIN_PA27     1
// #define IGNORE_PIN_PA28     1
// #define IGNORE_PIN_PB02     1
// #define IGNORE_PIN_PB03     1

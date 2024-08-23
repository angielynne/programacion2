/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package com.mycompany.condicionales;

import java.util.Scanner;

/**
 *
 * @author Sala de Sistemas
 */
public class Condicionales {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese su apellido: ");
        String apellido = scanner.nextLine();

        System.out.print("Ingrese su edad: ");
        int edad = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Ingrese su sexo (Masculino/Femenino): ");
        String sexo = scanner.nextLine();

        if (edad >= 18) {
            System.out.println("Es mayor de edad.");
        } else {
            System.out.println("Es menor de edad.");
        }

        if ("Masculino".equalsIgnoreCase(sexo)) {
            System.out.println("Es un Hombre.");
        } else if ("Femenino".equalsIgnoreCase(sexo)) {
            System.out.println("Es una Mujer.");
        } else {
            System.out.println("Sexo no reconocido.");
        }

        
    }
}

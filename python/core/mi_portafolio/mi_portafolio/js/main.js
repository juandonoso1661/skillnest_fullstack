// Esperar a que el HTML esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {

  // ==========================================
  // 1. MODO CLARO / OSCURO
  // ==========================================

  const themeToggleBtn = document.getElementById("theme-toggle");
  const themeIcon = document.getElementById("theme-icon");

  const actualizarIconoTema = () => {
    if (!themeIcon) return;

    const modoOscuro = document.documentElement.classList.contains("dark");

    themeIcon.className = modoOscuro
      ? "fas fa-sun text-yellow-400"
      : "fas fa-moon text-gray-600";
  };

  try {
    const temaGuardado = localStorage.getItem("portfolio-theme");

    if (
      temaGuardado === "dark" ||
      (!temaGuardado &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  } catch (error) {
    console.warn("No se pudo recuperar el tema guardado.");
  }

  actualizarIconoTema();

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", () => {
      document.documentElement.classList.toggle("dark");

      const modoOscuro =
        document.documentElement.classList.contains("dark");

      actualizarIconoTema();

      try {
        localStorage.setItem(
          "portfolio-theme",
          modoOscuro ? "dark" : "light"
        );
      } catch (error) {
        console.warn("No se pudo guardar la preferencia de tema.");
      }
    });
  }


  // ==========================================
  // 2. MENÚ DE NAVEGACIÓN MÓVIL
  // ==========================================

  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  const mobileLinks = document.querySelectorAll(".mobile-link");

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener("click", () => {
      const estaOculto = mobileMenu.classList.toggle("hidden");

      mobileMenuBtn.setAttribute(
        "aria-expanded",
        String(!estaOculto)
      );
    });

    mobileLinks.forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
        mobileMenuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }


  // ==========================================
  // 3. BARRA DE PROGRESO DE SCROLL
  // ==========================================

  const progressBar = document.getElementById("scroll-progress");

  if (progressBar) {
    const actualizarProgreso = () => {
      const alturaTotal =
        document.documentElement.scrollHeight - window.innerHeight;

      const progreso =
        alturaTotal > 0
          ? (window.scrollY / alturaTotal) * 100
          : 0;

      progressBar.style.width = `${progreso}%`;
    };

    window.addEventListener("scroll", actualizarProgreso);
    actualizarProgreso();
  }


  // ==========================================
  // 4. FILTRAR PROYECTOS
  // ==========================================

  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {

      filterBtns.forEach((boton) => {
        boton.classList.remove(
          "active",
          "bg-blue-600",
          "text-white"
        );

        boton.setAttribute("aria-pressed", "false");
      });

      btn.classList.add(
        "active",
        "bg-blue-600",
        "text-white"
      );

      btn.setAttribute("aria-pressed", "true");

      const filtro = btn.getAttribute("data-filter");

      projectCards.forEach((card) => {
        const categorias =
          (card.getAttribute("data-category") || "").split(" ");

        const coincide =
          filtro === "all" || categorias.includes(filtro);

        card.style.display = coincide ? "flex" : "none";
      });
    });
  });


  // ==========================================
  // 5. VENTANA MODAL DE PROYECTOS
  // ==========================================

  const modal = document.getElementById("project-modal");
  const closeModalBtn = document.getElementById("close-modal-btn");

  const modalTitle = document.getElementById("modal-title");
  const modalDescription = document.getElementById("modal-description");
  const modalTech = document.getElementById("modal-tech");

  const abrirModal = (card) => {
    if (!modal || !card) return;

    if (modalTitle) {
      modalTitle.textContent =
        card.getAttribute("data-title") || "Proyecto";
    }

    if (modalDescription) {
      modalDescription.textContent =
        card.getAttribute("data-description") || "";
    }

    if (modalTech) {
      modalTech.textContent =
        card.getAttribute("data-tech") || "";
    }

    modal.classList.add("open");
    document.body.style.overflow = "hidden";

    if (closeModalBtn) {
      closeModalBtn.focus();
    }
  };

  const cerrarModal = () => {
    if (!modal) return;

    modal.classList.remove("open");
    document.body.style.overflow = "";
  };

  document.querySelectorAll(".open-modal-btn").forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const tarjeta = event.currentTarget.closest(".project-card");
      abrirModal(tarjeta);
    });
  });

  if (closeModalBtn) {
    closeModalBtn.addEventListener("click", cerrarModal);
  }

  if (modal) {
    modal.addEventListener("click", (event) => {
      if (event.target === modal) {
        cerrarModal();
      }
    });
  }

  // Cerrar la ventana con Escape
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && modal?.classList.contains("open")) {
      cerrarModal();
    }
  });


  // ==========================================
  // 6. ACORDEÓN DE EJERCICIOS
  // ==========================================

  const accordionHeaders =
    document.querySelectorAll(".accordion-header");

  accordionHeaders.forEach((header) => {
    header.addEventListener("click", () => {
      const contenido = header.nextElementSibling;
      const icono = header.querySelector("i");

      if (!contenido) return;

      const estabaOculto = contenido.classList.toggle("hidden");

      header.setAttribute(
        "aria-expanded",
        String(!estabaOculto)
      );

      if (icono) {
        icono.classList.toggle("rotate-180", !estabaOculto);
      }
    });
  });


  // ==========================================
  // 7. COPIAR CORREO
  // ==========================================

  const copyEmailBtn = document.getElementById("copy-email-btn");
  const emailElement = document.getElementById("email-text");

  if (copyEmailBtn && emailElement) {
    copyEmailBtn.addEventListener("click", async () => {
      const correo = emailElement.textContent.trim();
      const textoOriginal = copyEmailBtn.textContent;

      try {
        await navigator.clipboard.writeText(correo);

        copyEmailBtn.textContent = "¡Copiado!";
        copyEmailBtn.classList.remove("bg-blue-600");
        copyEmailBtn.classList.add("bg-green-600");

        setTimeout(() => {
          copyEmailBtn.textContent = textoOriginal;
          copyEmailBtn.classList.remove("bg-green-600");
          copyEmailBtn.classList.add("bg-blue-600");
        }, 2000);

      } catch (error) {
        // Alternativa si el navegador no permite copiar
        window.location.href = `mailto:${correo}`;
      }
    });
  }


  // ==========================================
  // 8. FORMULARIO DE CONTACTO
  // ==========================================

  const contactForm = document.getElementById("contact-form");
  const formStatus = document.getElementById("form-status");

  if (contactForm && formStatus) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();

      formStatus.textContent =
        "Este formulario es una demostración y no envía mensajes. " +
        "Puedes contactarme directamente por correo electrónico.";

      formStatus.className =
        "text-sm text-center font-medium mt-2 text-blue-600 dark:text-blue-400 block";

      contactForm.reset();
    });
  }

});